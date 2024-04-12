#FUNCION QUE CONVIERTA UN NUMERO DECIMAL EN BINARIO Y OTRA QUE CONVIERTA UN NUMERO BINARIO EN DECIMAL.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# EJERCICIO20.PY (6-26)

# Función para convertir un número binario a decimal
def para_decimal(num):
    # Se convierte el número a una lista y se invierte el orden
    num = list(num)[::-1]
    # Se realiza la conversión de binario a decimal
    return sum(int(num[i]) * 2 **i for i in range(len(num)))

# Función para convertir un número decimal a binario
def para_binario(num):
    # Se realiza la conversión de decimal a binario y se retorna en formato string
    return bin(num)[2:]

# Se solicita al usuario ingresar un número binario
num_binario = input("Ingrese un número binario: ")
# Se muestra el resultado de la conversión a decimal
print(para_decimal(num_binario))

# Se solicita al usuario ingresar un número decimal
num_decimal = int(input("Ingrese un número decimal: "))
# Se muestra el resultado de la conversión a binario
print(para_binario(num_decimal))
