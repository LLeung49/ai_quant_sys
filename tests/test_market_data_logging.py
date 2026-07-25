import importlib.util
import sys
import types
from datetime import date as calendar_date
from pathlib import Path

import pytest
import pymysql


SCRIPT_PATH = Path(__file__).parents[1] / 'src' / 'data_ingestion' / '1-行情数据采集.py'
SCRIPT_DIR = str(SCRIPT_PATH.parent)


def load_market_module_with_fake_xtquant():
    """Import the collector without requiring the local QMT installation."""
    fake_xtdata = types.SimpleNamespace(
        download_history_data=lambda *args, **kwargs: None,
        get_market_data_ex=lambda *args, **kwargs: {},
    )
    fake_xtquant = types.ModuleType('xtquant')
    fake_xtquant.xtdata = fake_xtdata
    previous_xtquant = sys.modules.get('xtquant')
    sys.modules['xtquant'] = fake_xtquant
    sys.path.insert(0, SCRIPT_DIR)
    try:
        spec = importlib.util.spec_from_file_location('market_data_collector', SCRIPT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(SCRIPT_DIR)
        if previous_xtquant is None:
            sys.modules.pop('xtquant', None)
        else:
            sys.modules['xtquant'] = previous_xtquant


def raise_timeout(*args, **kwargs):
    raise TimeoutError('QMT timeout')


class FakeCursor:
    def __init__(self, error=None, close_error=None):
        self.error = error
        self.close_error = close_error
        self.closed = False

    def executemany(self, sql, rows):
        if self.error:
            raise self.error

    def close(self):
        self.closed = True
        if self.close_error:
            raise self.close_error


class FakeConnection:
    def __init__(
        self,
        cursor_error=None,
        cursor_close_error=None,
        rollback_error=None,
        close_error=None,
    ):
        self.cursor_instance = FakeCursor(cursor_error, cursor_close_error)
        self.rollback_error = rollback_error
        self.close_error = close_error
        self.rollback_calls = 0
        self.closed = False

    def cursor(self):
        return self.cursor_instance

    def commit(self):
        pass

    def rollback(self):
        self.rollback_calls += 1
        if self.rollback_error:
            raise self.rollback_error

    def close(self):
        self.closed = True
        if self.close_error:
            raise self.close_error


class OneRowDataFrame:
    def __len__(self):
        return 1

    def iterrows(self):
        yield '20250101', {
            'open': 1.0,
            'high': 2.0,
            'low': 0.5,
            'close': 1.5,
            'volume': 100,
            'amount': 1000.0,
        }


def return_one_valid_row(*args, **kwargs):
    return {'600519.SH': OneRowDataFrame()}


def read_only_log(log_dir):
    log_files = list(log_dir.glob('行情数据采集_*.log'))
    assert len(log_files) == 1
    return log_files[0].read_text(encoding='utf-8')


def test_download_exception_is_logged_and_reraised(tmp_path, monkeypatch):
    module = load_market_module_with_fake_xtquant()
    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)
    monkeypatch.setattr(module.xtdata, 'download_history_data', raise_timeout)

    with pytest.raises(TimeoutError, match='QMT timeout'):
        module.download_and_save('600519.SH', '20250101')

    log_files = list(tmp_path.glob('行情数据采集_*.log'))
    assert len(log_files) == 1
    log_text = log_files[0].read_text(encoding='utf-8')
    assert '股票=600519.SH' in log_text
    assert '开始日期=20250101' in log_text
    assert '阶段=下载历史数据' in log_text
    assert '代码位置=1-行情数据采集.py:' in log_text
    assert '错误=TimeoutError: QMT timeout' in log_text
    assert 'Traceback (most recent call last)' not in log_text

    for handler in module._get_logger().handlers:
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path)):
            handler.close()
            module._get_logger().removeHandler(handler)


def test_database_exception_rolls_back_logs_and_closes_resources(monkeypatch, tmp_path):
    module = load_market_module_with_fake_xtquant()
    connection = FakeConnection(cursor_error=RuntimeError('DB down'))
    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)
    monkeypatch.setattr(module, 'get_connection', lambda: connection)
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(RuntimeError, match='DB down'):
        module.download_and_save('600519.SH', '20250101')

    assert connection.rollback_calls == 1
    assert connection.closed is True
    assert connection.cursor_instance.closed is True
    assert '写入 MySQL' in read_only_log(tmp_path)

    for handler in module._get_logger().handlers:
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path)):
            handler.close()
            module._get_logger().removeHandler(handler)


def test_deadlock_retries_with_a_new_connection_and_recovers(monkeypatch, tmp_path):
    module = load_market_module_with_fake_xtquant()
    deadlock = pymysql.err.OperationalError(1213, 'deadlock found')
    failed_connection = FakeConnection(cursor_error=deadlock)
    successful_connection = FakeConnection()
    connections = iter([failed_connection, successful_connection])
    waits = []

    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)
    monkeypatch.setattr(module, 'get_connection', lambda: next(connections))
    monkeypatch.setattr(module, 'time', types.SimpleNamespace(sleep=waits.append))
    monkeypatch.setattr(
        module, 'random', types.SimpleNamespace(uniform=lambda start, end: 0), raising=False
    )
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    assert module.download_and_save('600519.SH', '20250101') == ('600519.SH', 1)
    assert failed_connection.rollback_calls == 1
    assert failed_connection.closed is True
    assert failed_connection.cursor_instance.closed is True
    assert successful_connection.closed is True
    assert waits == [0.2]
    assert 'attempt=1/5 wait=0.200s' in read_only_log(tmp_path)


def test_deadlock_reraises_after_five_attempts(monkeypatch):
    module = load_market_module_with_fake_xtquant()
    connections = [
        FakeConnection(
            cursor_error=pymysql.err.OperationalError(1213, 'deadlock found')
        )
        for _ in range(5)
    ]
    waits = []

    monkeypatch.setattr(module, 'get_connection', lambda: connections.pop(0))
    monkeypatch.setattr(module, 'time', types.SimpleNamespace(sleep=waits.append))
    monkeypatch.setattr(
        module, 'random', types.SimpleNamespace(uniform=lambda start, end: 0), raising=False
    )
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(pymysql.err.OperationalError, match='deadlock found'):
        module.download_and_save('600519.SH', '20250101')

    assert waits == [0.2, 0.4, 0.8, 1.6]


def test_non_deadlock_operational_error_is_not_retried(monkeypatch):
    module = load_market_module_with_fake_xtquant()
    connection = FakeConnection(
        cursor_error=pymysql.err.OperationalError(1205, 'lock wait timeout')
    )
    get_connection_calls = 0

    def get_connection_once():
        nonlocal get_connection_calls
        get_connection_calls += 1
        return connection

    monkeypatch.setattr(module, 'get_connection', get_connection_once)
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(pymysql.err.OperationalError, match='lock wait timeout'):
        module.download_and_save('600519.SH', '20250101')

    assert get_connection_calls == 1
    assert connection.rollback_calls == 1
    assert connection.closed is True


def test_cursor_close_failure_still_closes_connection(monkeypatch):
    module = load_market_module_with_fake_xtquant()
    connection = FakeConnection(cursor_close_error=RuntimeError('cursor close failed'))
    monkeypatch.setattr(module, 'get_connection', lambda: connection)
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(RuntimeError, match='cursor close failed'):
        module.download_and_save('600519.SH', '20250101')

    assert connection.cursor_instance.closed is True
    assert connection.closed is True


def test_rollback_failure_logs_and_preserves_database_exception(monkeypatch, tmp_path):
    module = load_market_module_with_fake_xtquant()
    connection = FakeConnection(
        cursor_error=RuntimeError('DB down'),
        rollback_error=RuntimeError('rollback failed'),
    )
    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)
    monkeypatch.setattr(module, 'get_connection', lambda: connection)
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(RuntimeError, match='DB down'):
        module.download_and_save('600519.SH', '20250101')

    assert connection.rollback_calls == 1
    assert connection.closed is True
    assert 'rollback failed' in read_only_log(tmp_path)
    assert 'DB down' in read_only_log(tmp_path)

    for handler in module._get_logger().handlers:
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path)):
            handler.close()
            module._get_logger().removeHandler(handler)


@pytest.mark.parametrize(
    ('cursor_close_error', 'connection_close_error', 'cleanup_message'),
    [
        (RuntimeError('cursor close failed'), None, 'cursor close failed'),
        (None, RuntimeError('connection close failed'), 'connection close failed'),
    ],
)
def test_cleanup_failure_during_database_error_preserves_original_exception(
    monkeypatch,
    tmp_path,
    cursor_close_error,
    connection_close_error,
    cleanup_message,
):
    module = load_market_module_with_fake_xtquant()
    connection = FakeConnection(
        cursor_error=RuntimeError('DB down'),
        cursor_close_error=cursor_close_error,
        close_error=connection_close_error,
    )
    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)
    monkeypatch.setattr(module, 'get_connection', lambda: connection)
    monkeypatch.setattr(module.xtdata, 'get_market_data_ex', return_one_valid_row)

    with pytest.raises(RuntimeError, match='DB down'):
        module.download_and_save('600519.SH', '20250101')

    log_text = read_only_log(tmp_path)
    assert cleanup_message in log_text
    assert 'DB down' in log_text
    assert connection.closed is True

    for handler in module._get_logger().handlers:
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path)):
            handler.close()
            module._get_logger().removeHandler(handler)


def test_logger_replaces_stale_daily_file_handler(monkeypatch, tmp_path):
    module = load_market_module_with_fake_xtquant()
    monkeypatch.setattr(module, 'LOG_DIR', tmp_path)

    class FirstDay:
        @classmethod
        def today(cls):
            return calendar_date(2025, 1, 1)

    class SecondDay:
        @classmethod
        def today(cls):
            return calendar_date(2025, 1, 2)

    monkeypatch.setattr(module, 'date', FirstDay)
    logger = module._get_logger()
    stale_handler = next(
        handler for handler in logger.handlers
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path))
    )

    monkeypatch.setattr(module, 'date', SecondDay)
    logger = module._get_logger()
    active_paths = [
        Path(handler.baseFilename).name
        for handler in logger.handlers
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path))
    ]

    assert stale_handler not in logger.handlers
    assert stale_handler.stream is None
    assert active_paths == ['行情数据采集_20250102.log']

    for handler in logger.handlers:
        if getattr(handler, 'baseFilename', '').startswith(str(tmp_path)):
            handler.close()
            logger.removeHandler(handler)
