#

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos la función length_words que toma una oración como argumento
def length_words(sentence):
    # Dividimos la oración en palabras usando el método split()
    words = sentence.split()
    # Utilizamos la función map() para aplicar la función len() a cada palabra
    lengths = map(len, words)
    # Creamos un diccionario que asocia cada palabra con su longitud
    return dict(zip(words, lengths))

# Solicitamos al usuario que introduzca una oración
sentence = input("Por favor, introduce una oración: ")
# Imprimimos el resultado de aplicar la función length_words a la oración introducida por el usuario
print(length_words(sentence))
