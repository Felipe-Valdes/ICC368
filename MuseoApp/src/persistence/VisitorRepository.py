# src/persistence_layer/data_access.py

from sqlalchemy import create_engine
import pandas as pd
from src.database.config import CONNECTION_STRING

class VisitorRepository:
    
    def __init__(self):
        self.engine = create_engine(CONNECTION_STRING)

    # Requerimiento 1
    # Obtiene a los visitantes, juntos a sus recorridos por su exhibición, en un rango de fechas y ordenados por fecha de inicio.
    def get_visitors_and_exhibition_between_dates_ordered_by_start_date(self, fecha_inicio, fecha_termino):
        query = """
        SELECT 
            Usuario.nombre AS Nombre_Usuario,
            Usuario.apellidos AS Apellidos_Usuario,
            Usuario.correo AS Correo_Usuario,
            Exhibicion.nombre AS Nombre_Exhibicion,
            Recorrido.fechaInicio AS Fecha_Ingreso,
            Recorrido.fechaTermino AS Fecha_Salida
        FROM 
            Recorrido
        JOIN 
            Usuario ON Recorrido.Usuarioid = Usuario.id
        JOIN 
            Exhibicion ON Recorrido.Exhibicionid = Exhibicion.id
        WHERE 
            Recorrido.fechaInicio BETWEEN %s AND %s
        ORDER BY 
            Recorrido.fechaInicio;
        """
        return pd.read_sql_query(query, self.engine, params=(fecha_inicio, fecha_termino))

    # Requerimiento 4s
    # Obtiene a los visitantes en un rango de fechas.
    def get_visitors_by_date_range(self, start_date, end_date):
        query = """
                SELECT 
                    DATE(Recorrido.fechaInicio) AS Fecha,
                    COUNT(DISTINCT Recorrido.Usuarioid) AS Cantidad_Visitantes
                FROM 
                    Recorrido
                WHERE 
                    Recorrido.fechaInicio BETWEEN %s AND %s
                GROUP BY 
                    Fecha
                ORDER BY 
                    Fecha;
                """
        return pd.read_sql_query(query, self.engine, params=(start_date, end_date))

    # Requerimiento 8
    # Obtiene a los visitantes ordenados por cantidad de asistencias a las exhibiciones.
    def get_visitors_ordered_by_number_of_attendances(self):
        query = """
        SELECT 
            Usuario.nombre AS Nombre_Visitante,
            Usuario.apellidos AS Apellidos_Visitante,
            COUNT(Recorrido.id) AS Numero_Asistencias
        FROM 
            Recorrido
        JOIN 
            Usuario ON Recorrido.Usuarioid = Usuario.id
        GROUP BY 
            Usuario.id
        ORDER BY 
            Numero_Asistencias DESC;
        """
        return pd.read_sql_query(query, self.engine)
    


