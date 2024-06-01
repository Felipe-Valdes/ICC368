# src/database_layer/config.py
import pymysql
from sqlalchemy import create_engine

USERNAME = ''
PASSWORD = ''
HOST = '200.13.4.226'  # usualmente 'localhost' o una dirección IP
DATABASE = 'Museo'

CONNECTION_STRING = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
