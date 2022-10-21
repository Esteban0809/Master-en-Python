"""
SET es un tipo de dato, prr tener una coleccion de valores,
pero no tiene ni indice ni orden
"""
personas = {
    "Victor",
    "Manolo",
    "francisco",
}
personas.add("Paco")
personas.remove("francisco")

print(type(personas))
print (personas)