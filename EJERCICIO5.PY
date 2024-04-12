#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitamos al usuario que ingrese su renta anual y la convertimos a float
renta = float(input("¿Cual es tu renta anual? "))

# Evaluamos la renta en los diferentes rangos y asignamos el tipo de impuesto correspondiente
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo=20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

# Calculamos el monto del impuesto y lo mostramos al usuario
impuesto = renta * tipo / 100
print(f"Tienes que pagar {impuesto} lps")
