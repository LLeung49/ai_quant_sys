import json
from data_ingestion.db_config import execute_query

rows = execute_query("SHOW FULL PROCESSLIST")
print(json.dumps(rows, ensure_ascii=False, default=str, indent=2))
