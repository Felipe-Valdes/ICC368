from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class ThemeRepository:
    
    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    # Requerimiento 9
    # Obtiene a las temáticas, juntos a sus exhibiciones.
    def get_themes_and_expositions(self):
        query = """
        SELECT 
            T.nombre AS Tematica,
            E.nombre AS Exhibicion,
            E.descripcion AS Descripcion_Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion
        FROM 
            Tematica T
        JOIN 
            Tematica_Exhibicion TE ON T.id = TE.Tematicaid
        JOIN 
            Exhibicion E ON TE.Exhibicionid = E.id
        ORDER BY 
            T.nombre, E.nombre;
        """
        return pd.read_sql_query(query, self.engine)