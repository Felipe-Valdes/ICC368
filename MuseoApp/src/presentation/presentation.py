# src/presentation_layer/presentation.py
import matplotlib.pyplot as plt
import MuseoApp.src.business.VisitorService as VisitorService
# Define dos fecha de inicio y término, y obtiene los visitantes en ese rango
start_date = '2021-01-01'
end_date = '2021-12-31'

VisitorService = VisitorService.MuseumService()
visitors = VisitorService.get_visitors_by_date(start_date, end_date)

