#programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Inicializamos un diccionario vacío para almacenar la información de la persona
persona = {}

# Creamos una variable booleana para controlar el bucle while
continuar = True

# Iniciamos un bucle while que se ejecutará mientras 'continuar' sea True
while continuar:

    # Solicitamos al usuario que introduzca la clave del dato que quiere añadir
    clave = input('¿Qué dato quieres introducir? ')

    # Solicitamos al usuario que introduzca el valor correspondiente a la clave
    valor = input(clave + ': ')

    # Añadimos la clave y el valor al diccionario 'persona'
    persona[clave] = valor

    # Imprimimos el diccionario 'persona' para que el usuario pueda ver la información que ha introducido
    print(persona)

    # Preguntamos al usuario si desea continuar añadiendo información
    # Si la respuesta es 'Si' o 'si', 'continuar' seguirá siendo True y el bucle while se repetirá
    # Si la respuesta es diferente, 'continuar' se convertirá en False y el bucle while se detendrá
    continuar = input('¿Quieres añadir más información (Si/No)? ').lower() == "si"
