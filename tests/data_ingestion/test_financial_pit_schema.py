"""Existing PIT tables gain nullable metrics without rewriting old rows."""

from morning_conference.sector_rotation2.research.financial.schema import (
    apply_schema_ddl,
)


def test_migration_adds_only_missing_metric_columns() -> None:
    class Cursor:
        def __init__(self):
            self.statements = []

        def execute(self, sql):
            self.statements.append(sql)

        def fetchall(self):
            return [("stock_code",), ("source_verified",), ("eps",)]

        def close(self):
            pass

    class Connection:
        def __init__(self):
            self.cur = Cursor()

        def cursor(self):
            return self.cur

        def commit(self):
            pass

    connection = Connection()
    apply_schema_ddl(connection)
    alters = [sql for sql in connection.cur.statements if sql.startswith("ALTER TABLE")]
    assert not any("ADD COLUMN eps " in sql for sql in alters)
    assert any("ADD COLUMN roe " in sql for sql in alters)
    assert any("ADD COLUMN metric_available_at " in sql for sql in alters)
    assert any("ADD COLUMN metric_lineage_json " in sql for sql in alters)
