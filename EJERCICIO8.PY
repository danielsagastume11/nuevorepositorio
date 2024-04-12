# programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitamos al usuario que introduzca la altura del triángulo
num = int(input("Introduce la altura del triangulo (entero positivo:) "))

# Verificamos que el número ingresado sea positivo
if num > 0:
    # Iteramos sobre el rango del número ingresado, incrementando de 2 en 2
    for i in range(1, num+1, 2):
        # Dentro de cada iteración, volvemos a iterar desde 'i' hasta 0, decrementando de 2 en 2
        for j in range(i, 0 , -2):
            # Imprimimos 'j' y un espacio en blanco, sin pasar a la siguiente línea
            print(j, end=" ")
        # Pasamos a la siguiente línea una vez terminada la iteración interna
        print("")
else:
    # Si el número ingresado no es positivo, imprimimos un mensaje de error
    print("El número ingresado no es un entero positivo.")
