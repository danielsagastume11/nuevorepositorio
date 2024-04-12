#programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita al usuario que introduzca una palabra
palabra = input("Introduce una palabra: ")

# Verifica si el input del usuario es un número
if palabra.isdigit():
    # Si es un número, imprime un mensaje de error
    print("Error: Has introducido un número. Por favor, introduce una palabra.")
else:
    # Si no es un número, se ejecuta el siguiente bloque de código
    # El rango se establece en la longitud de la palabra -1 (para obtener el último índice de la cadena), 
    # hasta -1 (para llegar al primer índice), y -1 indica que el rango va en orden inverso.
    for i in range(len(palabra)-1,-1,-1):
        # Imprime cada carácter de la cadena en orden inverso
        print(palabra[i])