"""
Ejerccio 7: hacer un programa que muestre todos los numeros imlares
entre dos numeros que decida el usuario
"""


numero1 = int(input("Introduce un numero:"))
numero2 = int(input("introdce el siguiente numero:"))

if numero1 < numero2:

    for x in range (numero1, (numero2+1)):

        if x%2==0:
            print (f"{x} es PAR")
else:
    print(f"{x}es impar")
    print("el primer numero debe ser mayor que el segundo")