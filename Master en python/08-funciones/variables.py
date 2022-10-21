"""
Variables locales : Se definen dentro de la función y no
se puede usar fuera de ella, solo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función
y están disponibles dentro y fuera de ellas.

"""

#Variable global

frase = "Ni los genios son tan genios ni los mediocres son tan mediocres"


print(frase)

def holaMundo():
    frase = " Hola mundo!"
    print("Dentro de lafunción :")
    print(frase)

    year = 2021
    print(year)
    global website
    website = "victorroblesweb.es"
    print("Dentro :", website)


    return  " Dato vevuelto" + " " + str (year)

print (holaMundo())
print("FUERA. ",website)
