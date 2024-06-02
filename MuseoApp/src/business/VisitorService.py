import src.persistence.VisitorRepository as VisitorRepository

class VisitorService:

    def __init__(self):
        self.visitor_repository = VisitorRepository.VisitorRepository()

    # Requerimiento 1
    # Obtiene a los visitantes, juntos a sus recorridos por su exhibición, en un rango de fechas y ordenados por fecha de inicio.
    # Posteriormente, transforma el resultado a json.
    def get_json_visitors_and_exhibition_between_dates_ordered_by_start_date(self, start_date, end_date):
        visitors = self.visitor_repository.get_visitors_and_exhibition_between_dates_ordered_by_start_date(start_date, end_date)
        # Parsea los datos a json
        return visitors.to_json(orient='records')
    
    # Requerimiento 4
    # Obtiene a los visitantes ordenados por cantidad de asistencias.
    # Posteriormente, transforma el resultado a json.
    def get_json_visitors_ordered_by_number_of_attendances(self):
        visitors = self.visitor_repository.get_visitors_ordered_by_number_of_attendances()
        # Parsea los datos a json
        return visitors.to_json(orient='records')
    
    # Requerimiento 6
    # Obtiene a los visitantes en un rango de fechas.
    # Posteriormente, transforma el resultado a json.
    def get_json_visitors_by_date_range(self, start_date, end_date):
        visitors = self.visitor_repository.get_visitors_by_date_range(start_date, end_date)
        # Parsea los datos a json
        return visitors.to_json(orient='records')