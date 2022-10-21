"""
Ejercicio 1. Hacer un programa que tenga una lista 
de 8 numeros enteros y haga lo siguiente:
(hecho)- Recorrer la lista y mostrarla 
(hecho)-Hacer funcion que recorra listas de numeros y devuelva un string
(hecho)- Ordenarla y mostrarla
(hecho)- Mostrar su longitud
- buscar algun elemento que el usuario pida por teclado

"""

#Crear lista
numeros = [ 13,64,52,73,21,7,91,63]
# Crear función que recorra lista y devuelva string
def mostrarLista(lista):
    resultado = " "

    for elemento in lista:
        resultado += "elemento:  " + str (elemento)
        resultado += "\n"

    return resultado
# Recorrer y mostrar
print("#################### Recorreer y mostrar #######################")
"""
for numero in numeros :
    print(numero)

"""
print(mostrarLista(["Victor", "Juan","Pepe"]))

# Ordenar y mostrar
print("#################### Ordenar y mostrar #######################")
numeros.sort()
print(mostrarLista(numeros))
#Mostrar su longitud
print("#################### Mostrar su longitud #######################")
print(len(numeros))

# Busqueda en la lista
print("#################### Busqueda en la Lista #######################")
try:
    busqueda = int(input(" Introduce el numero:"))
    comprobar = isinstance(busqueda, int)
    while not comprobar  or busqueda <= 0:
        busqueda =int( input("Introduce el numero: "))
    else: 
        print(f"Has introducido el {busqueda}")

    print(f"######### Buscar en la lista el numero {busqueda}#############")   


    search = numeros.index(busqueda)
    print(f" El número buscado existe en la lista , es el indice: {search}")

except:
    print("El número no está en la lista , lo siento")

