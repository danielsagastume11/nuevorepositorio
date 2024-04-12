#programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	    0.85
#Naranja	0.70


import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos un diccionario con las frutas y sus precios
frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}

# Solicitamos al usuario la fruta y los kilos que desea
fruta, kg = input('¿Qué fruta quieres? ').title(), float(input('¿Cuántos kilos? '))

# Imprimimos el precio si la fruta está en el diccionario, si no, un mensaje de error
print(kg, 'kilos de', fruta, 'valen', frutas.get(fruta, 0)*kg, '€') if fruta in frutas else print("Lo siento, la fruta", fruta, "no está disponible.")
