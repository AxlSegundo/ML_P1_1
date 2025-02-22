import numpy as np

# 1
array = np.arange(15)
print("Array unidimensional:", array)

# 2
matriz_aleatoria = np.random.randint(0, 11, size=(3, 3))
print("Matriz aleatoria 3x3:\n", matriz_aleatoria)

# 3
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(f"Los valores a ocupar para las operaciones son {array1} y {array2}")
suma = array1 + array2
print("Suma:", suma)

resta = array1 - array2
print("Resta:", resta)

multiplicacion = array1 * array2
print("Multiplicación elemento por elemento:", multiplicacion)

producto_escalar = np.dot(array1, array2)
print("Producto escalar:", producto_escalar)

# 4
array_estadisticas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

media = np.mean(array_estadisticas)
print("Media:", media)

desviacion_estandar = np.std(array_estadisticas)
print("Desviación estándar:", desviacion_estandar)

valor_maximo = np.max(array_estadisticas)
print("Valor máximo:", valor_maximo)