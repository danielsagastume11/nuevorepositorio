#pedir al usuario dos numeros y mostrar en pantalla su division si el divisor es 0, debe mostrar error.

import os
os.system('cls' if os.name == 'nt' else 'clear')

try:
    # Solicitamos al usuario que introduzca el primer número, que será el dividendo
    num1 = int(input("Ingrese el dividendo: "))

    # Solicitamos al usuario que introduzca el segundo número, que será el divisor
    num2 = int(input("Ingrese el divisor: "))

    # Intentamos realizar la división
    print("Resultado: ", num1/num2)
except ZeroDivisionError:
    # Si el divisor es cero, mostramos un mensaje de error
    print("Error, No puede dividir por 0.")
except ValueError:
    # Si el valor ingresado no es un número, mostramos un mensaje de error
    print("Error, Debe ingresar un número.")
