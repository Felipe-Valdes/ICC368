# main.py

from src.business.business_logic import BusinessLogic
from src.presentation.presentation import Presentation

# Instanciar las clases de lógica de negocios y presentación
business_logic = BusinessLogic()
presentation = Presentation()

# Obtener datos
start_date = '2023-01-01'
end_date = '2023-12-31'
df = business_logic.get_visitors_by_exhibition(start_date, end_date)

# Mostrar datos
print(df)

# Graficar datos
presentation.plot_visitors_by_date(df)
