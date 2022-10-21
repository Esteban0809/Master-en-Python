"""
# Condicional IF

SI se_cumple_esta_condicion:
    ejecutar grupo de instrucciones
SI NO:
Se ejecutan otro grupo de  instrucciones
if condicion:
    instruciones
else:
otras instruciones
#operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que



"""
"""
#ejemplo1
print("################## EJEMPLO1 #######################")

color = "Rojo"
#color= input( " Adivina cual es mi color favorito: ")

if color =="rojo":
    print("Enhorbuena")
    print("El color es Rojo")
else:
    print("El color es incorecto")



print("\n################## EJEMPLO 2 #######################")


year = 2020
int (input("¿en que año estamos?: "))

if year <2021:
    print("Estamos de 2021 en adelante !¡ ")
else:
    print("Es un año anterior a 2021")
    """
"""
 # ejemplo 3
print("\n################## EJEMPLO 3 #######################")
nombre = "Esteban"
ciudad = "Pontevedra"
continente = "Europa"
edad = 43
mayoria_edad = 18

if edad>=mayoria_edad:
    print(f"{nombre} es mayor de edad!!!") 

    if continente != "Europa":
        print("El usuario No es Europeo")
    else:
        print(f"es Europeo y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")

#Ejemplo 4
print("\n################## EJEMPLO 4 #######################")
"""
"""
dia = int(input("introduce el numero del  dia de la semana: "))

if dia==1:
    print("Es lunes")
else: 
    if dia == 2:
        print("es martes")
    else:
        if dia ==3:
            print("es miercoles")
        else:
            if dia==4:
                print("es jueves")
            else:
                if dia == 5 :
                    print("es viernes")
                else:
                    print("es fin de semana")
    

dia = int(input("introduce el numero del  dia de la semana: "))
if dia == 1:
    print("es lunes")
elif dia ==2:
    print("es martes")
elif dia ==3:
    print("es miercoles")
elif dia == 4:
    print("es jueves")
elif dia == 5 :
    print("es viernes")
else:
    print("ya es fin de semana")

        #Ejemplo 5
print("\n################## EJEMPLO 5 #######################")
edad_minima=18
edad_maxima=65
edad_oficial = int(input("tieness edad de trabajar? introduce tu edad:"))

if edad_oficial >= 18 and edad_oficial<=65:
    print("esta en edad de trabajar!!")
else:
    print("no está en edad de trabajar")

 #Ejemplo 6
print("\n################## EJEMPLO 6 #######################")

pais = "Rusia"

if pais == "Mexico" or pais =="España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!!!")
else:
    print(f"{pais} no es de habla hispana: ")




#Ejemplo 7
print("\n################## EJEMPLO 7 #######################")


pais = "España"

if not  pais == "Mexico" or pais =="España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana!!!")
else:
    print(f"{pais} no es de habla hispana: ")
"""


#Ejemplo 8
print("\n################## EJEMPLO 8 #######################")

pais = "EEUU"

if pais != "Mexico" and pais !="España" and pais !="Colombia":
    print(f"{pais} no es un pais de habla hispana!!!")
else:
    print(f"{pais} si es un pais de habla hispana :)")