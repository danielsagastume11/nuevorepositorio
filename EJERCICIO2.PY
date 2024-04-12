# almacenar una cadena de caracteres para una contrseña y pregunte al usuario por ella, para ver si coincide o no.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# La función input() permite al usuario introducir una cadena de texto. En este caso, se le pide al usuario que introduzca una nueva contraseña.
llave = input("Introduce una nueva contraseña: ")

# Se le pide al usuario que introduzca la contraseña que acaba de crear.
contra = input("Introduce la contraseña: ")

# Comparamos las dos contraseñas. Utilizamos el método lower() para convertir ambas contraseñas a minúsculas y asegurarnos de que la comparación no sea sensible a las mayúsculas.
if llave.lower() == contra.lower():
    # Si las contraseñas coinciden, se imprime este mensaje.
    print("contraseña correcta")
else:
    # Si las contraseñas no coinciden, se imprime este otro mensaje.
    print("La contraseña no coincide")
