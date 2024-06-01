# src/presentation_layer/presentation.py

import matplotlib.pyplot as plt

class Presentation:
    def plot_visitors_by_date(self, df):
        plt.figure(figsize=(10, 6))
        plt.plot(df['Fecha_Ingreso'], df['Nombre_Visitante'], marker='o')
        plt.title('Cantidad de Visitantes por Día')
        plt.xlabel('Fecha de Ingreso')
        plt.ylabel('Nombre de Visitante')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
