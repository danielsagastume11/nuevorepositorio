# programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita al usuario un número entero y lo convierte a int
num = int(input("Introduzca un numero entero: "))

# Convierte el número a cadena una sola vez para usarlo después
num_str = str(num)

# Comprueba si el número es par
if num % 2 == 0:
    # Si el número es par, imprime este mensaje
    print("El numero " + num_str + " es par")
else:
    # Si el número no es par (es decir, es impar), imprime este mensaje
    print("El numero " + num_str + " es impar")

