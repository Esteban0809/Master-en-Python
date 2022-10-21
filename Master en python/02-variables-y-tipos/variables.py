"""
Una variable es un conetnedor de informacion
que dentro guardará un dato ,se pueden crear
muchas variables y que cada una tenga un dato distinto
"""

texto = "Master en python"
texto2 = ("con Esteban Ferreiro")
numero = 44
decimal= 6,7
#mostrar variables

print(texto)
print(texto2)
print(numero)
print(decimal)
print("___________________________________________________")
#reasignacion de valores
numero = 77
decimal = 8.9
print(numero)
print(decimal)

#concatenacion

nombre = "Esteban"
apellido="Ferreiro "
web= "esteban.ferreiro@hotmail.es"
print(nombre+" "+ apellido+" "+web)
print(f"{nombre} {apellido} - {web}")
print("hola me llamo {} {} y mi web es: {} ".format(nombre, apellido, web))
print(nombre, apellido  ,web)


