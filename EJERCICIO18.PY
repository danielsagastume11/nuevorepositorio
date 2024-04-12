#función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos una funcion llamada "square" que toma una lista como argumento
def square(lista):
    # Creamos una lista vacía para almacenar los resultados
    list = []
    # Iteramos sobre cada elemento en la lista de entrada
    for i in lista:
        # Agregamos el cuadrado del elemento actual a la lista de resultados
        list.append(i**2)
    # Devolvemos la lista de resultados
    return list

# Solicitamos al usuario que ingrese los números, separados por comas
user_input = input("Por favor, ingrese los números, separados por comas: ")
# Convertimos la entrada del usuario en una lista de strings, dividiendo la entrada por las comas
user_list = user_input.split(",")
# Convertimos cada string en la lista a un número flotante
user_list = [float(num) for num in user_list]

# Llamamos a la función "square" con la lista de números del usuario e imprimimos el resultado
print(square(user_list))
