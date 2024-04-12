#programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

import os
os.system('cls' if os.name == 'nt' else 'clear')

def celebrar_edades():
    # Solicita al usuario que introduzca su edad y convierte la entrada en un número entero
    edad = int(input("Introduce tu edad: "))
    
    # Para cada número en el rango desde 0 hasta la edad introducida
    for i in range(edad):
        # Imprime un mensaje indicando el número de años cumplidos
        # Convertimos el número de años a string para poder concatenarlo con el resto del mensaje
        print("Has cumplido " + str(i+1) + " años")

# Llamamos a la función
celebrar_edades()
