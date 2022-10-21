"""
#FOR    

for variable in elemento_iterable (lista, rango, etc.)
    BLOQUE DE INSTRUCCIONES    



contador = 0
resultado = 0

for contador in range ( 0, 10):
    print("voy por el numero" +" "+ str(contador))

    resultado +=  contador
print(f"el resultado es:{resultado}")


"""


# Ejemplo tablas de multiplicar

print("\n#################### EJEMPLO##########################")

numero_usuario = int(input("¿de que numero quieres la tabla?: "))

if numero_usuario<1:
   numero_usuario = 1
print(f"\n############tabla de multiplicar del número {numero_usuario}###########")

for numero_tabla in range (1,11):
    if numero_usuario == 45:
        print("no se pueden mostrar numeros prohibidos")
        break
    
        

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print( " tabla finalizada. " )