#programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Inicializa un diccionario vacío llamado "cesta". Este diccionario almacenará los artículos y sus precios.
cesta = {}

# Inicializa una variable booleana llamada "continuar" en True. Esta variable se usará para controlar el bucle while.
continuar = True

# Inicia un bucle while que continuará hasta que el usuario decida parar (es decir, cuando "continuar" sea False).
while continuar:
    # Solicita al usuario que introduzca un artículo y lo almacena en la variable "item".
    item = input('Introduce un artículo: ')

    # Solicita al usuario que introduzca el precio del artículo y lo almacena en la variable "precio" como un número flotante.
    precio = float(input('Introduce el precio de ' + item + ': '))

    # Añade el artículo y su precio al diccionario "cesta".
    cesta[item] = precio

    # Pregunta al usuario si desea continuar añadiendo artículos. Si el usuario responde "Si", el bucle continuará. Si no, el bucle se detendrá.
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"

# Inicializa una variable "coste" en 0. Esta variable almacenará el coste total de los artículos.
coste = 0

# Imprime "Lista de la compra".
print('Lista de la compra')

# Inicia un bucle for que recorre todos los artículos y sus precios en el diccionario "cesta".
for item, precio in cesta.items():
    # Imprime el artículo y su precio.
    print(item, '\t', precio)

    # Suma el precio del artículo al coste total.
    coste += precio

# Imprime el coste total de los artículos.
print('Coste total: ', coste)