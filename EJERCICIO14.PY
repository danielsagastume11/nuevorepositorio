# programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Se crea una lista con los números del 1 al 10.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Se utiliza un bucle for para recorrer la lista de números.
# La función reversed() se utiliza para invertir el orden de la lista.
# En cada iteración, se imprime el número actual seguido de una coma y un espacio.
for numero in reversed(numeros):
    print(numero, end=", ")
