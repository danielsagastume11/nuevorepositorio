# programa que pida al usuario una palabra y la muestre 10 veces.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitamos al usuario que introduzca una palabra
palabra = input("Introduce una palabra: ")

# Solicitamos al usuario que introduzca un número, que determinará cuántas veces se repetirá la palabra
repeticiones = int(input("Introduce un número de repeticiones: "))

# Creamos un bucle que se ejecutará tantas veces como el número introducido por el usuario
for i in range(repeticiones):
    # En cada iteración del bucle, imprimimos la palabra
    print(palabra)
