import numpy as np
import pandas as pd

# 1. Crear un array con 100 valores aleatorios
valores_aleatorios = np.random.rand(100)
print("Array con 100 valores aleatorios:\n", valores_aleatorios)

# 2. Convertir el array en una columna de un DataFrame
df = pd.DataFrame(valores_aleatorios, columns=['Valores Aleatorios'])
print("\nDataFrame con una columna de valores aleatorios:\n", df.head())  # Mostrar las primeras 5 filas

# 3. Añadir una segunda columna con el cuadrado de los valores aleatorios
df['Cuadrado'] = df['Valores Aleatorios'] ** 2
print("\nDataFrame con columna 'Cuadrado':\n", df.head())  # Mostrar las primeras 5 filas

# 4. Guardar el DataFrame en un archivo CSV
df.to_csv('P1_1/Practica/datos_aleatorios.csv', index=False)
print("\nDataFrame guardado en 'datos_aleatorios.csv'")