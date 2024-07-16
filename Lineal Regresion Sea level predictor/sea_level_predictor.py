# creamos la segunda linea
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
             # Leer datos desde el archivo
             df = pd.read_csv("epa-sea-level.csv")

             # nombres de columnas
             y = df["CSIRO Adjusted Sea Level"]
             x = df["Year"]

             # Crear gráfico de dispersión
             fig, axxx = plt.subplots()
             axxx.scatter(
                 x,
                 y)  # Corregir el uso de axxx.scatter en lugar de plot.scatter

             # Crear primera línea de mejor ajuste
             res = linregress(x, y)
             x_prediccion = pd.Series([i for i in range(1880, 2051)])

             #  Crea una serie de años de 1880 a 2050 para predecir los valores de la línea de mejor ajuste.
             y_prediccion = res.slope * x_prediccion + res.intercept  # Calcula los valores predichos utilizando la ecuación de la línea de mejor ajuste.
             plt.plot(x_prediccion, y_prediccion, "r")  # dibuja la linea

             #Crear segunda linea en base a datos de la columna años desde el año 2000 en adelante
             new_df = df.loc[df['Year'] >= 2000]
             nueva_x = new_df['Year']
             nueva_y = new_df['CSIRO Adjusted Sea Level']
             res_2 = linregress(nueva_x, nueva_y)
             x_prediccion2 = pd.Series([i for i in range(2000, 2051)])
             y_prediccion2 = res_2.slope * x_prediccion2 + res_2.intercept
             plt.plot(x_prediccion2, y_prediccion2, 'green')

             # Agregar etiquetas y título
             axxx.set_xlabel('Year')  # Agregar una etiqueta x al gráfico.
             axxx.set_ylabel(
                 'Sea Level (inches)')  # Agregar una etiqueta y al gráfico.
             axxx.set_title("Rise in Sea Level")

             # Guardar gráfico y devolver datos para pruebas (No modificar)
             # plt.savefig('sea_level_plot.png')

             plt.savefig(r'sea_level_plot.png', dpi=300, bbox_inches='tight')

             return plt.gca()


draw_plot()
