# función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definimos una función para aplicar un descuento a un precio
def apply_discount(price, discount=20):  # Establecemos un descuento por defecto del 20%
    # Calculamos el precio final después de aplicar el descuento
    return price - price * discount / 100

# Definimos una función para aplicar el IVA a un precio
def apply_IVA(price, percentage=21):  # Establecemos un IVA por defecto del 21%
    # Calculamos el precio final después de aplicar el IVA
    return price + price * percentage / 100

# Definimos una función para calcular el precio total de una cesta de la compra
def price_basket(basket, function):
    # Inicializamos el total a 0
    total = 0
    # Recorremos todos los elementos de la cesta
    for price, discount in basket.items():
        # Aplicamos la función (descuento o IVA) al precio del producto y lo añadimos al total
        total += function(price, discount)
    # Devolvemos el precio total de la cesta
    return total

# Pedimos al usuario que introduzca el precio de la compra
price = int(input('Introduce el precio de la compra: '))

# Creamos un diccionario con el precio y el descuento
basket = {price: 20}  # Usamos el descuento por defecto del 20%
# Calculamos el precio después del descuento y lo mostramos
print('El precio de la compra tras aplicar los descuentos es: ', price_basket(basket, apply_discount))

# Creamos un diccionario con el precio y el IVA
basket = {price: 21}  # Usamos el IVA por defecto del 21%
# Calculamos el precio después del IVA y lo mostramos
print('El precio de la compra tras aplicar el IVA es: ', price_basket(basket, apply_IVA))
