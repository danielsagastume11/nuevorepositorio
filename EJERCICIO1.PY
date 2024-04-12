#programa que calcula la edad y muestra si es mayor de edad o no

import os
os.system('cls' if os.name == 'nt' else 'clear')

# EJERCICIO1.py (6-14)

# Definimos una función llamada verificar_edad
def verificar_edad():
    # Solicitamos al usuario que ingrese su edad y la convertimos a entero
    edad = int(input("¿Cual es su edad? "))
    # Si la edad es menor a 18
    if edad < 18:
        # Imprimimos un mensaje indicando que es menor de edad
        print("Eres menor de edad. ")
    else:
        # Si la edad es 18 o más, imprimimos un mensaje indicando que es mayor de edad
        print("Eres mayor de edad.")

# Llamamos a la función verificar_edad para ejecutarla
verificar_edad()
