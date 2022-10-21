import os, shutil


# Crear Carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print(" El directorio ya existe")

"""
# Copiar
ruta_original =  "./mi_carpeta"
ruta_nueva =  "./mi_carpeta_COPIADA"

#print(rut_alternativa)
shutil.copytree(ruta_original, ruta_nueva )

# Eliminar
os.rmdir('./mi_carpeta_COPIADA')
"""
print("Contenido de mi carpeta: ")
contenido = os.listdir("./mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero: "+fichero)