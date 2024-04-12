# programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica.

import os
os.system('cls' if os.name == 'nt' else 'clear')
# Solicita al usuario una muestra de números separados por comas
muestra = input("Introduce una muestra de números separados por comas: ")

# Convierte la cadena de texto en una lista, donde cada elemento es un número ingresado por el usuario
muestra = muestra.split(',')

# Calcula la cantidad de números ingresados por el usuario
n = len(muestra)

# Convierte cada elemento de la lista en un número entero
muestra = [int(i) for i in muestra]

# Calcula la suma de los números ingresados y la suma de los cuadrados de los números ingresados
suma = sum(muestra)
suma_cuadrados = sum(i**2 for i in muestra)

# Calcula la media de los números ingresados
media = suma/n

# Calcula la desviación estándar de los números ingresados
desviacion = (suma_cuadrados/n - media**2)**(1/2)

# Imprime la media y la desviación estándar
print('La media es', media, ', y la desviacion tipica es', desviacion)
