from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class ArtefactRepository:

    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    