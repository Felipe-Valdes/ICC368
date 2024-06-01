# src/persistence_layer/data_access.py

from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class DataAccess:
    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    def execute_query(self, query, params=None):
        return pd.read_sql_query(query, self.engine, params=params)
