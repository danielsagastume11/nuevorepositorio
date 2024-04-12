"""función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos una función para calcular el área de un círculo
def area_del_circulo(radio):
    pi = 3.1415 # Definimos el valor de pi
    return pi*radio**2 # Calculamos el área del círculo y la retornamos

# Definimos una función para calcular el volumen de un cilindro
def volumen_cilindro(radio, alto):
    return area_del_circulo(radio)*alto # Calculamos el volumen del cilindro y lo retornamos

# Pedimos al usuario que ingrese el radio del cilindro
radio = float(input("Ingrese el radio del cilindro: "))

# Pedimos al usuario que ingrese la altura del cilindro
alto = float(input("Ingrese la altura del cilindro: "))

# Imprimimos el volumen del cilindro utilizando las funciones definidas anteriormente
print(volumen_cilindro(radio, alto))
