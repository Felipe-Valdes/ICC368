# main.py
import src.business.VisitorService as VisitorService

if __name__ == '__main__':
    # Define dos fecha de inicio y término, y obtiene los visitantes en ese rango
    start_date = '2021-01-01'
    end_date = '2021-12-31'

    museum_service = VisitorService.VisitorService()
    visitors = museum_service.get_visitors_and_exhibition_between_dates_ordered_by_start_date(start_date, end_date)

    # Imprime los visitantes
    print(visitors)