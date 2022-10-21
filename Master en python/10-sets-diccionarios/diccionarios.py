"""
Diccionario:
es un tipo de dato que almacena un conjunto de datos.
En formato clave valor.
es parecido a un array asociativo o un objeto json
"""
persona = {
    "nombre":"Victor",
    "apellidos": "Robles",
    "web":"victoroblesweb.com"

}

print(persona["web"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email':' antonio@antonio.com'
    },
    {
        'nombre':'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre':'Salvador',
        'email': 'salvador@salvador.com'
    },
]

contactos[0]['nombre'] = "Antoñito"
print(contactos[0]['nombre']) 

print("\nlistado de contactos: ")

print("----------------------------------------------------------------------")

for contacto in contactos :
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto ['email']}")
    print("----------------------------------------------------------------------")