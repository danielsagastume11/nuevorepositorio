# función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3.

import os
os.system('cls' if os.name == 'nt' else 'clear')

# Importamos las funciones mean y stdev de la biblioteca statistics.
# mean calcula la media de los datos y stdev calcula la desviación estándar.
from statistics import mean, stdev

# Definimos una función llamada atipico que toma como parámetro una muestra de datos.
def atipico(muestra):
    # Calculamos la media de la muestra.
    media = mean(muestra)
    # Calculamos la desviación estándar de la muestra.
    desviacion = stdev(muestra)
    # Definimos una función f que toma como parámetro un número.
    def f(n):
        # Calculamos la puntuación z del número, que es la distancia entre el número y la media en términos de desviación estándar.
        puntuacion = (n - media) / desviacion
        # Si la puntuación z es menor que -3 o mayor que 3, el número es atípico, por lo que devolvemos True. Si no, devolvemos False.
        return (puntuacion < -3) or (puntuacion > 3)
    # Devolvemos la función f.
    return f

# Definimos una función llamada datos_atipicos que toma como parámetro una muestra de datos.
def datos_atipicos(muestra):
    # Filtramos la muestra con la función atipico y convertimos el resultado en una lista.
    # Esto nos da una lista de los datos atípicos en la muestra.
    return list(filter(atipico(muestra), muestra))

# Imprimimos los datos atípicos de la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000].
print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
