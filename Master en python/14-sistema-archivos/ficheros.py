from genericpath import isfile
from io import open
import pathlib
import shutil

# Abrir archivo
ruta =  str(pathlib.Path().absolute())+"/fichero.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir dentro de un archivo
archivo.write("*************** Soy un texto metido desde python *************************\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta =  str(pathlib.Path().absolute())+"/fichero.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()

#for elemento in contenido :
    #print(contenido)

    # Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista :
    frase
    lista_frase = frase.split()
    print(lista_frase)
    print("-"+ frase.center(100))
"""
# copiar
ruta_original = ruta =  str(pathlib.Path().absolute())+"/fichero.txt"
ruta_nueva =  str(pathlib.Path().absolute())+"/copiado.txt"
rut_alternativa = "../07-ejercicios/fichero_copiado88.txt"
#print(rut_alternativa)
shutil.copyfile(ruta_original, rut_alternativa )

"""

# Mover
"""
ruta_original = str(pathlib.Path().absolute()) +"/copiado.txt"
ruta_nueva =   str(pathlib.Path().absolute()) +"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar archivos
import os
"""
ruta_nueva =   str(pathlib.Path().absolute()) +"/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""
#Comprobar si un archivo existe o no
import os.path

#print(os.path.abspath("../"))
ruta_comprobar = os.path.abspath("./") +  "/fichero_texto.txt"
ruta_comprobar = "fichero_texto.txt"

if os.path.isfile(ruta_comprobar):
    print(" El archivo existe")
else:
    print(" El archivo no existe")




