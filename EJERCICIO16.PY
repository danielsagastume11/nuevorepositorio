#una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definición de la función greet
def greet():
    """
    Esta es una cadena de documentación, también conocida como docstring.
    Se utiliza para explicar en detalle lo que hace la función.
    En este caso, la función greet muestra el mensaje '!Hola amiga!' por pantalla.
    """
    
    # La función print() muestra el mensaje '!Hola amiga!' por pantalla
    print('!Hola amiga!')
    
    # La instrucción return finaliza la función. En este caso, como no devuelve nada, se puede omitir.
    return

# Llamada a la función greet. Cuando se llama a esta función, se ejecuta el código dentro de la función,
# mostrando el mensaje '!Hola amiga!' por pantalla.
greet()
