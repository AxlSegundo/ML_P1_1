import pandas as pd

# 1
data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Sofía'],
    'Edad': [20, 21, 19, 22, 20],
    'Calificación': [8.5, 5.0, 7.0, 6.5, 9.0]
}

df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# 2
df['Aprobó'] = df['Calificación'] >= 6
print("\nDataFrame con columna 'Aprobó':\n", df)

# 3
aprobados = df[df['Aprobó']]
print("\nEstudiantes que aprobaron:\n", aprobados)

# 4
csv_data = """Nombre,Edad,Calificacion
Ana,20,8.5
Luis,21,5.0
Maria,19,7.0
Carlos,22,6.5
Sofia,20,9.0
Carlos,20,8.7
David,23,9.5
"""

with open('P1_1/Practica/estudiantes.csv', 'w') as file:
    file.write(csv_data)

# Leer el archivo CSV y mostrar las primeras 5 filas
df_csv = pd.read_csv('P1_1/Practica/estudiantes.csv')
print("\nPrimeras 5 filas del DataFrame leído desde CSV:\n", df_csv.head())