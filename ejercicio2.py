import pandas as pd
from tabulate import tabulate

# Cargar la base de datos en un DataFrame
df = pd.read_csv("base_datos_hospital.csv", header=0)

# Filtrar hombres mayores de 80 años con COVID-19 atendidos por el doctor Pérez
hombres_covid_perez = df[(df['Genero'] == 'Masculino') & 
                          (df['Edad'] > 80) & 
                          (df['Diagnostico'].str.contains('Covid19', case=False)) & 
                          (df['Medico_Asignado'].str.contains('Perez', case=False))]

# Comprobar si hay resultados
if not hombres_covid_perez.empty:
    # Mostrar los resultados de forma tabulada con todas las columnas
    print("\nHombres mayores de 80 años con COVID-19 atendidos por el doctor Pérez:")
    print(tabulate(hombres_covid_perez, headers='keys', tablefmt='grid'))
else:
    print("\nNo se encontraron hombres mayores de 80 años con COVID-19 atendidos por el doctor Pérez.")

#Eavemaria profe que conchas de mangos no?
