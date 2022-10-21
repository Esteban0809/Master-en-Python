"""
LISTAS (arrays)
son colecciones o conjuntos de datos/valores, bajo un unico 
nombre.
para acceder a esos valores podemos usar un indice númerico.
"""

from ast import In


pelicula = "Batman"

# Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(('2pac','Drake','Jenifer Lopez'))
years = list(range (2020,2050))
variada = [ "victor", 30,4.4, True, " Texto"]

"""
print(cantantes)
print(peliculas)
print(years)
print(variada)


#Indices
pelicula = " otra cosa"
peliculas[1] = " Gran Torino"
peliculas[2] = " el Hobbit"

print(peliculas)

print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

# Añadir elementos a lista
cantantes.append("Kase O")
cantantes.append("Natos y Waor")
print(cantantes)

# Recorrer Lista


nueva_pelicula  = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula : ")

    if nueva_pelicula != "parar" :
        peliculas.append(nueva_pelicula)


print("\n*****************LISTADO PELICULAS***************************")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") 

    # Listas Multidimensionales
    """
print("\n*******************LISTADO DE CONTACTOS***************************************")
contactos = [
        [
            'Antonio',
            'antonio@antonio.com'
        ],
        [
            'Luis',
            'luis@luis.com'
        ],
        [
            'Salvador'
            'salvador@.com'
        ]
    ]
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("nombre:" + elemento)
        else:
            print("Email : " + elemento)

        print("\n")
#print(contactos[1][1])





