#programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

import os
os.system('cls' if os.name == 'nt' else 'clear')
# Solicita al usuario que ingrese una palabra
palabra= input("Introduce una palabra: ")

# Crea una lista con las vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Para cada vocal en la lista de vocales
for vocal in vocales:
    # Inicializa un contador en 0
    tiempo = 0
    # Para cada letra en la palabra ingresada por el usuario
    for letra in palabra:
        # Si la letra es igual a la vocal en la iteración actual
        if letra == vocal:
            # Incrementa el contador en 1
            tiempo += 1
    # Imprime la vocal y el número de veces que aparece en la palabra
    print("La vocal " + vocal + " aparece " + str(tiempo) + " veces")
