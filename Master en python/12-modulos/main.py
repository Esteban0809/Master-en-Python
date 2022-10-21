"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/library/math.html#module-math

podemos conseguir modulos que ya vienen en el lenguaje,
modulosen internet y tambíen podemo crear nuestros propios 
modulos.
"""
# Importar modulo propio
# import mimodulo
#from mimodulo import holaMundo
from random import random
from mimodulo import*

print(holaMundo("Esteban Ferreiro Web"))
print(calculadora(3,5,True))

# Modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S ")
print(" Mi fecha personalizada",fecha_personalizada)

print(datetime.datetime.now().timestamp())

#  Modulo matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print("Número pi:", float (math.pi))
print("Redondear", math.floor(6.56798))

# Modulo random
import random
print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))