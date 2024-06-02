from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class ExpositionRepository:
    
    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)


    # Requerimiento 2
    # Obtiene a las exhibiciones, juntos a los artefactos que contienen, ordenados por fecha de inicio.
    def get_expositions_and_artefacts_ordered_by_start_date(self):
        query = """
        SELECT 
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion,
            A.nombre AS Artefacto,
            A.descripcion AS Descripcion_Artefacto
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

    # Requerimiento 7
    # Obtiene a las exhibiciones, juntos a la cantidad de recorridos que se han realizado en ellas.
    def get_expositions_and_total_tours(self):
        query = """
        SELECT 
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion,
            COUNT(R.id) AS Total_Recorridos
        FROM 
            Recorrido R
        JOIN 
            Exhibicion E ON R.Exhibicionid = E.id
        GROUP BY 
            E.id
        ORDER BY 
            Total_Recorridos DESC;
        """
        return pd.read_sql_query(query, self.engine)
    

    # Requerimiento 7, intervalo de fechas
    # Obtiene a las exhibiciones, juntos a la cantidad de recorridos que se han realizado en ellas, en un rango de fechas.
    def get_expositions_and_total_tours_between_dates(self, start_date, end_date):
        query = """
        SELECT 
            E.nombre AS Exhibicion,
            E.fechaInicio AS Fecha_Inicio_Exhibicion,
            E.fechaTermino AS Fecha_Termino_Exhibicion,
            COUNT(R.id) AS Total_Recorridos
        FROM 
            Recorrido R
        JOIN 
            Exhibicion E ON R.Exhibicionid = E.id
        WHERE 
            R.fechaInicio BETWEEN %s AND %s
        GROUP BY 
            E.id
        ORDER BY 
            Total_Recorridos DESC;
        """
        return pd.read_sql_query(query, self.engine, params=(start_date, end_date))
    
    # Requerimiento 10
    # Obtiene a las exhibiciones, juntos a sus empresas visitantes.
    def get_expositions_and_visiting_companies(self):
        query = """
            SELECT 
                E.nombre AS Exhibicion,
                E.descripcion AS Descripcion_Exhibicion,
                E.fechaInicio AS Fecha_Inicio_Exhibicion,
                E.fechaTermino AS Fecha_Termino_Exhibicion,
                GROUP_CONCAT(Empresa.nombre SEPARATOR ', ') AS Empresas_Visitantes
            FROM 
                Exhibicion E
            JOIN 
                Convenio C ON E.id = C.Exhibicionid
            JOIN 
                Empresa ON C.Empresaid = Empresa.id
            GROUP BY 
                E.nombre, E.descripcion, E.fechaInicio, E.fechaTermino;
            """
        return pd.read_sql_query(query, self.engine)
    