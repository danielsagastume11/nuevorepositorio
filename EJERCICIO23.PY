#programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Creamos un diccionario donde las claves son los números de los meses y los valores son los nombres de los meses.
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

# Creamos una función que recibe una fecha en formato dd/mm/aaaa y devuelve la fecha en formato dd de mes de aaaa
def convertir_fecha(fecha):
    # El método split divide la cadena de texto en una lista, usando como separador el carácter '/'
    fecha = fecha.split('/')
    # Imprime el día, el nombre del mes y el año. Para obtener el nombre del mes, se usa el número del mes como clave en el diccionario 'meses'.
    print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

# Solicitamos al usuario que introduzca una fecha
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')

# Llamamos a la función convertir_fecha pasándole la fecha introducida por el usuario
convertir_fecha(fecha)
