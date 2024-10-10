import pandas as pd
from tabulate import tabulate

# Cargar la base de datos en un DataFrame
df = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar personas de apellido Rodriguez mayores de 50 años con enfermedades diferentes a gripa y fractura
personas_rodriguez = df[(df['Apellido'].str.contains('Rodriguez', case=False)) & 
                         (df['Edad'] > 50) & 
                         (~df['Diagnostico'].str.contains('Gripe', case=False)) & 
                         (~df['Diagnostico'].str.contains('Fractura', case=False))]

# Comprobar si hay resultados
if not personas_rodriguez.empty:
    # Mostrar los resultados de forma tabulada con todas las columnas
    print("\nPersonas de apellido Rodríguez mayores de 50 años con enfermedades diferentes a gripa y fractura:")
    print(tabulate(personas_rodriguez, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron personas de apellido Rodríguez mayores de 50 años con enfermedades diferentes a gripa y fractura.")
