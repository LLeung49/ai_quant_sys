from data_ingestion.db_config import execute_update

execute_update("KILL QUERY 49634")
print("killed audit query 49634")
