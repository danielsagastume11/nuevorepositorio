# programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Primero, creamos una lista con los nombres de algunas asignaturas
lista =["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

# Luego, imprimimos la lista completa
print(lista)

# Podemos agregar un elemento al final de la lista usando el método append
lista.append("Informática")
print(lista) # Imprimimos la lista para verificar que "Informática" se ha añadido

# También podemos eliminar un elemento de la lista usando el método remove
lista.remove("Fisica")
print(lista) # Imprimimos la lista para verificar que "Fisica" se ha eliminado

# Podemos verificar cuántos elementos hay en la lista usando la función len
print("La lista tiene", len(lista), "elementos")

# También podemos acceder a un elemento específico de la lista a través de su índice
print("El primer elemento de la lista es", lista[0])

# Podemos ordenar los elementos de la lista en orden alfabético usando el método sort
lista.sort()
print("La lista ordenada es", lista)

# Finalmente, podemos invertir el orden de los elementos en la lista usando el método reverse
lista.reverse()
print("La lista invertida es", lista)
