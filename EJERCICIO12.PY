#programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Inicializamos las asignaturas y las notas
asignaturas = ["Matematicas", "Física", "Quimica", "Historia", "Lengua"]
notas = []

# Iteramos sobre cada asignatura
for asignatura in asignaturas:
    # Solicitamos al usuario que introduzca la nota de la asignatura y la agregamos a la lista de notas
    notas.append(float(input(f"¿Qué nota has sacado en {asignatura}? ")))

# Calculamos el promedio de las notas
promedio = sum(notas) / len(notas)

# Iteramos sobre cada asignatura y su correspondiente nota
for asignatura, nota in zip(asignaturas, notas):
    # Imprimimos la asignatura y la nota
    print(f"En {asignatura} has sacado {nota}")

# Imprimimos el promedio
print(f"Tu promedio general es: {promedio}")
