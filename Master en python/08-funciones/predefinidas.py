nombre = "Victor Robles"

#funciones generales
print( type (nombre))

#Dectectar tipado
comprobar = isinstance(nombre, int)
if comprobar :
    print("Esa variable es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

#Limpiar espacios
frase ="        mi contenido        "
print(frase)
print(frase.strip())

#Eliminar variables
year = 2022
print(year)
del year
#print(year)

#Comprobar variables vacia
texto = "   ff  "

if len(texto) <= 0:
    print("La variable está vacia")
else: 
     print("La variable tiene contenido:", len(texto))

#Encontrar caracteres
frase = "La vida es Bella "
print(frase.find("vida"))

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

#Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper)