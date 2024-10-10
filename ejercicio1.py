import pandas as pd
from tabulate import tabulate

# Cargar la base de datos en un DataFrame
df = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar mujeres mayores de 80 años con COVID-19
mujeres_covid = df[(df['Genero'] == 'Femenino') & (df['Edad'] > 80) & (df['Diagnostico'].str.contains('Covid19', case=False))]

# Comprobar si hay resultados
if not mujeres_covid.empty:
    # Mostrar los resultados de forma tabulada con todas las columnas
    print("\nMujeres mayores de 80 años con COVID-19:")
    print(tabulate(mujeres_covid, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron mujeres mayores de 80 años con COVID-19.")

#Profe Tania PILAS que en la BD hay nombres de hombres que salen con género femenino :D 