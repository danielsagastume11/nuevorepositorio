#función reciba un diccionario con la las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos una función para asignar la calificación correspondiente a cada nota
def grade(score):
    if score < 5:  # Si la nota es menor a 5
        return 'SS'  # La calificación es 'SS'
    elif score < 7:  # Si la nota es menor a 7
        return 'AP'  # La calificación es 'AP'
    elif score < 9:  # Si la nota es menor a 9
        return 'NT'  # La calificación es 'NT'
    elif score < 10:  # Si la nota es menor a 10
        return 'SB'  # La calificación es 'SB'
    else:  # Si la nota es 10
        return 'MH'  # La calificación es 'MH'

# Definimos una función para aplicar la función grade a las notas de cada asignatura
def apply_grade(scores):
    subjects = map(str.upper, scores.keys())  # Convertimos los nombres de las asignaturas a mayúsculas
    grades = map(grade, scores.values())  # Aplicamos la función grade a las notas
    return dict(zip(subjects, grades))  # Creamos un nuevo diccionario con las asignaturas y las calificaciones

# Solicitamos al usuario que ingrese las notas
scores = {}
while True:
    subject = input("Introduce el nombre de la asignatura (o 'salir' para terminar): ")
    if subject.lower() == 'salir':
        break
    score = float(input("Introduce la nota de la asignatura: "))
    scores[subject] = score

# Imprimimos las calificaciones
print(apply_grade(scores))