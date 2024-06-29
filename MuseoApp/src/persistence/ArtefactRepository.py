from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class ArtefactRepository:

    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)
    
    # Requerimiento 3, sin filtros
    # Obtiene a los artefactos, juntos a sus exhibiciones.
    def get_artefacts_and_exhibitions(self):
        query = """
        SELECT 
            A.nombre AS Artefacto,
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion
        FROM 
            Artefacto_Exhibicion AE
        JOIN 
            Artefacto A ON AE.Artefactoid = A.id
        JOIN 
            Exhibicion E ON AE.Exhibicionid = E.id
        ORDER BY 
            E.fechaInicio;
        """
        return pd.read_sql_query(query, self.engine)

    # Requerimiento 3, con filtro de id de artefacto 
    # Obtiene a los artefactos, juntos a sus exhibiciones, filtrando por id de artefacto.
    def get_artefacts_and_exhibitions_by_artefact_id(self, artefact_id):
        query = """
        SELECT 
            A.nombre AS Artefacto,
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion
        FROM 
            Artefacto_Exhibicion AE
        JOIN 
            Artefacto A ON AE.Artefactoid = A.id
        JOIN 
            Exhibicion E ON AE.Exhibicionid = E.id
        WHERE 
            A.id = %s
        ORDER BY 
            E.fechaInicio;
        """
        return pd.read_sql_query(query, self.engine, params=(artefact_id,))
    
    # Requerimiento 3, con filtro de rango de fechas
    # Obtiene a los artefactos, juntos a sus exhibiciones, en un rango de fechas.
    def get_artefacts_and_exhibitions_between_dates(self, start_date, end_date):
        query = """
        SELECT 
            A.nombre AS Artefacto,
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion
        FROM 
            Artefacto_Exhibicion AE
        JOIN 
            Artefacto A ON AE.Artefactoid = A.id
        JOIN 
            Exhibicion E ON AE.Exhibicionid = E.id
        WHERE 
            E.fechaInicio BETWEEN %s AND %s
        ORDER BY 
            E.fechaInicio;
        """
        return pd.read_sql_query(query, self.engine, params=(start_date, end_date))
    
    # Requerimiento 3, con filtro de rango de fechas y id de artefacto
    # Obtiene a los artefactos, juntos a sus exhibiciones, en un rango de fechas y filtrando por id de artefacto.
    def get_artefacts_and_exhibitions_between_dates_by_artefact_id(self, start_date, end_date, artefact_id):
        query = """
        SELECT 
            A.nombre AS Artefacto,
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion
        FROM 
            Artefacto_Exhibicion AE
        JOIN 
            Artefacto A ON AE.Artefactoid = A.id
        JOIN 
            Exhibicion E ON AE.Exhibicionid = E.id
        WHERE 
            E.fechaInicio BETWEEN %s AND %s
            AND A.id = %s
        ORDER BY 
            E.fechaInicio;
        """
        return pd.read_sql_query(query, self.engine, params=(start_date, end_date, artefact_id))
    
    
    # Requerimiento 5
    # Obtiene a los artefactos, juntos a su familia, ordenados por familia y nombre.
    def get_artefacts_ordered_by_family_and_name(self):
        query = """
        SELECT A.*, F.nombre AS Familia
            FROM Artefacto A
        JOIN Artefacto_Familia AF ON A.id = AF.Artefactoid
        JOIN Familia F ON AF.Familiaid = F.id
            ORDER BY F.nombre, A.nombre;
        """
        return pd.read_sql_query(query, self.engine)
    
    # Obtener solo todos los artefactos
    def get_artefacts(self):
        query = """
        SELECT * FROM Artefacto;
        """
        return pd.read_sql_query(query, self.engine)