# Capturar excepciones y manejar errores 
# en codigo susceptible a fallos/errores
"""
try:
    nombre = input ("¿Cual es tu nombre :")

    if len (nombre) > 1 :
        nombre_usuario = " El nombre es " + nombre
    print (nombre_usuario)
except: 
    print("Ha ocurrido un error, mete bien el nombre")   
else:
    print("Todo ha funcionado correctamente") 
finally:
    print("Fin de la iteración")


    # Multiples excepciones
from turtle import st

try:
    numero = int(input("Numero para elevar al cuadrado: "))
    print("el cuadrado es :" +str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas a enteros en el codigo!!")
#except ValueError:
    #print("introduce un numero correcto!!")
except Exception as e:
    print(type(e))
    print(" Ha ocurrido un error: ", type(e), __name__)
    from ast import Try
    """


    # Excepciones personalizadas o lanzar excepciones



try:
    nombre = input(" Introduce el nombre :")
    edad = int(input(" introduce la edad:"))

    if edad < 5 or edad > 110:
        raise ValueError(" La edad introducida no es real")
    elif len (nombre) <= 1:
        raise ValueError(" El nombre no está completo")
    else:
        print( f" Bienvenido al master en python {nombre}")
except ValueError:
    print(" Introduce los datos correctamente")
except Exception as e:
    print(" Existe un error")