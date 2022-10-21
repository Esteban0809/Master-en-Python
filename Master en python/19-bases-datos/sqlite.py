# importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()
cursor.execute("SELECT *FROM productos  WHERE precio >=300;")

# Crear tabla
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
titulo varchar(255), 
descripcion text, 
precio int(255)
);
""")

# Guardar cambios
conexion.commit

# Isertar datos
"""

cursor.execute(" INSERT INTO productos VALUES (null, 'Segundo producto', 'descripcion de mi producto',550)")
conexion.commit
"""
# Borrar registros
cursor.execute("DELETE FROM productos ;")
conexion.commit()

# Insertar muchos registros de golpe
productos = [ 
    (  "ordenador portatil", "Buen Pc", 700),
    (  "Telefono movil ", "Buen telefono", 140),
    (  "placa base", "Buen placa", 80),
    ( "tablet 15", "Buen tablet", 300),
    
]
cursor.executemany ("INSERT INTO productos VALUES (null,?,?,?)", productos )
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio =678 WHERE PRECIO=80")

# Listar datos
cursor.execute("SELECT *FROM productos  WHERE precio >=300;")

print(cursor)
productos = cursor.fetchall()

for producto in productos:
    print("ID", producto[0])
    print ("Titulo:",producto[1])
    print ("precio:",producto[2])
    print ("precio:",producto[3])
    print("\n")
cursor.execute("SELECT titulo FROM productos;")

producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()