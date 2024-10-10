import pandas as pd
from tabulate import tabulate

# Cargar la base de datos en un DataFrame
df = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar personas menores de edad con gripa en el año 2020
personas_gripa_2020 = df[(df['Edad'] < 18) & 
                          (df['Diagnostico'].str.contains('Gripe', case=False)) & 
                          (df['Fecha_Ingreso'] == 2020)]

# Comprobar si hay resultados
if not personas_gripa_2020.empty:
    # Mostrar los resultados de forma tabulada con todas las columnas
    print("\nPersonas menores de edad con gripa en el año 2020:")
    print(tabulate(personas_gripa_2020, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron personas menores de edad con gripa en el año 2020.")
