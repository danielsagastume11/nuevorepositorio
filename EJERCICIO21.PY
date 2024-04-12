#programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

import os
os.system('cls' if os.name == 'nt' else 'clear')
# Se define una clase llamada CurrencyConverter
class CurrencyConverter:

    # Esta es la función de inicialización que se llama cuando se crea un objeto de la clase
    def __init__(self):
        # Se inicializa un diccionario con tres divisas y su valor en dólares
        # Cada divisa es una clave del diccionario y su valor es otro diccionario que contiene el símbolo y el valor de la divisa
        self.coins = {'Euro': {'symbol': '€', 'value': 0.85},
                      'Dollar': {'symbol': '$', 'value': 1.00},
                      'Yen': {'symbol': '¥', 'value': 109.74}}

    # Se define una función lambda para convertir una cantidad de una divisa a otra
    # Si las divisas existen en el diccionario, se realiza la conversión y se redondea a dos decimales
    # Si una o ambas divisas no existen en el diccionario, se retorna un mensaje de error
    convert = lambda self, amount, from_currency, to_currency : round((amount/self.coins[from_currency.title()]['value']) * self.coins[to_currency.title()]['value'], 2) if from_currency.title() in self.coins and to_currency.title() in self.coins else "Una o ambas divisas no están disponibles."

    # Se define una función lambda para convertir el objeto a una cadena de texto
    # Se unen las claves del diccionario (las divisas) con comas y se retorna la cadena resultante
    __str__ = lambda self: ', '.join(self.coins.keys())

# Esta línea verifica si este archivo se está ejecutando directamente o se está importando como un módulo
if __name__ == "__main__":
    # Se crea un objeto de la clase CurrencyConverter
    converter = CurrencyConverter()
    # Se imprimen las divisas disponibles utilizando la función str del objeto
    print(f"Divisas disponibles: {converter}")
    # Se imprimen el resultado de la conversión utilizando la función convert del objeto
    # Se solicita al usuario que introduzca la cantidad que desea convertir y se convierte a float
    # Se solicita al usuario que introduzca la divisa de origen y de destino
    # Todo esto se hace directamente en la llamada a convert
    print(f"El resultado de la conversión es: {converter.convert(float(input('Introduce la cantidad que deseas convertir: ')), input('Introduce la divisa de origen: '), input('Introduce la divisa a la que deseas convertir: '))}")
