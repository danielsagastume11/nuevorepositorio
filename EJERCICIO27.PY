#función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importamos las funciones matemáticas que vamos a utilizar
from math import sin, cos, tan, exp, log

# Creamos un diccionario con las funciones matemáticas que vamos a utilizar
functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}

# Definimos una función que toma como parámetros una función matemática y un número entero
def apply_function(f, n):
    # Devolvemos un diccionario por comprensión aplicando la función matemática a cada número del rango
    return {i: functions[f](i) for i in range(1, n+1)}

# Definimos una función que va a actuar como calculadora
def calculator():
    # Pedimos al usuario que introduzca la función matemática y un número entero
    f, n = input('Introduce la función a aplicar (sin, cos, tan, exp, log): '), int(input('Introduce un entero positivo: '))
    # Aplicamos la función matemática al número entero y mostramos los resultados
    print(*[f"{i}\t{j}" for i, j in apply_function(f, n).items()], sep='\n')

# Llamamos a la función calculadora
calculator()