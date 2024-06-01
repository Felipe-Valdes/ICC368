# src/business_layer/business_logic.py

from src.persistence.data_acess import DataAccess

class BusinessLogic:
    def __init__(self):
        self.data_access = DataAccess()

    def get_visitors_by_exhibition(self, start_date, end_date):
        query = """
        SELECT 
            Usuario.nombre AS Nombre_Visitante,
            Usuario.apellidos AS Apellidos_Visitante,
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
        return self.data_access.execute_query(query, [start_date, end_date])

    # Otros métodos de negocio según sea necesario
