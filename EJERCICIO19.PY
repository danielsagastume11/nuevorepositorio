# programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos una función que toma un texto como entrada
def cadena_texto(text): 
    # Usamos la función split para dividir el texto en palabras y usamos un diccionario para contar las ocurrencias de cada palabra
    cadena = {i: text.split().count(i) for i in text.split()}
    return cadena  # Devolvemos el diccionario

# Definimos una función que toma un diccionario como entrada
def mostrar_repetidas(cadena): 
    # Usamos la función max para encontrar la palabra con la mayor frecuencia
    max_palabra, max_freq = max(cadena.items(), key=lambda x: x[1])
    return max_palabra, max_freq  # Devolvemos la palabra y su frecuencia

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'  # Definimos el texto

# Llamamos a las funciones y mostramos los resultados
print(cadena_texto(text))  
print(mostrar_repetidas(cadena_texto(text)))  

