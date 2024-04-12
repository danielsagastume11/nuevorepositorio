#programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

import os
os.system('cls' if os.name == 'nt' else 'clear')

def cuenta_letras(frase, letra):
    # Convertimos la frase y la letra a minúsculas para que la función sea insensible a mayúsculas
    frase = frase.lower()
    letra = letra.lower()

    contador = 0

    # Recorremos cada caracter de la frase
    for i in frase:
        # Si el caracter es igual a la letra que estamos buscando, incrementamos el contador
        if i == letra:
            contador += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra,contador,frase))

frase = input("Introduce una frase:")
letra = input("Introduce una letra:")

cuenta_letras(frase, letra)
