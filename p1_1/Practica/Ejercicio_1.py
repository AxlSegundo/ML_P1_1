def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return suma, resta, multiplicacion, division


def es_par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        print(f"{numero} es un número impar.")

def fibonacci(n):
    secuencia = [0, 1]
    for _ in range(n - 2):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

entero = 10
print(type(entero))
flotante = 3.14
print(type(flotante))
cadena = "Hola, Python"
print(type(cadena))
booleano = True
print(type(booleano))

# Pruebas
a = int(input("Dame un valor para realizar las operaciones: "))
b = int(input("Dame un valor para realizar las operaciones: "))
print("Operaciones básicas:", operaciones_basicas(a, b))

numero =  int(input("Dame un valor: "))
es_par_o_impar(numero)

print("Primeros 10 números de la secuencia de Fibonacci:", fibonacci(10))