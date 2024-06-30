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
        return visitors.to_dict(orient='records')


    # Requerimiento 4
    # Obtiene a los visitantes en un rango de fechas.
    # Posteriormente, transforma el resultado a json.
    def get_json_visitors_by_date_range(self, start_date, end_date, period):
        visitors = self.visitor_repository.get_visitors_by_date_range(start_date, end_date, period)
        # Parsea los datos a json
        return visitors.to_dict(orient='records')
    
    # Requerimiento 6: Calcula el crecimiento de visitantes en porcentaje entre periodos de tiempo.
    def get_json_visitors_growth_percentage(self):
        visitors = self.visitor_repository.get_visitors_by_year_month()
        
        # Calcular el porcentaje de crecimiento
        growth_percentage = visitors['Cantidad_Visitantes'].pct_change() * 100
        
        # Crear una lista de diccionarios con los resultados
        growth_list = []
        for i in range(len(visitors)):
            if i == 0:
                growth_dict = {
                    'Mes': int(visitors['Mes'].iloc[i]),
                    'Anio': int(visitors['Anio'].iloc[i]),
                    'Cantidad_Visitantes': int(visitors['Cantidad_Visitantes'].iloc[i]),  # Asegura que sea int
                    'Crecimiento_Porcentaje': 0
                }
                growth_list.append(growth_dict)
                continue
            growth_dict = {
                'Mes': int(visitors['Mes'].iloc[i]),
                'Anio': int(visitors['Anio'].iloc[i]),
                'Cantidad_Visitantes': int(visitors['Cantidad_Visitantes'].iloc[i]),  # Asegura que sea int
                'Crecimiento_Porcentaje': growth_percentage.iloc[i]
            }
            growth_list.append(growth_dict)
        return growth_list
    
        
    # Requerimiento 8
    # Obtiene a los visitantes ordenados por cantidad de asistencias.
    # Posteriormente, transforma el resultado a json.
    def get_json_visitors_ordered_by_number_of_attendances(self):
        visitors = self.visitor_repository.get_visitors_ordered_by_number_of_attendances()
        # Parsea los datos a json
        return visitors.to_dict(orient='records')
