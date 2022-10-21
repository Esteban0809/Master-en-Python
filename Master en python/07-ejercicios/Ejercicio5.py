""""
Ejercicio 5. Hacer un programa que muestre todos los nueros 
entre dos numeros que diga el usuario
"""

numero1 = int(input("introduce el primer numero: "))
numero2 = int(input("introduce el segundo numero: "))

if numero1 < numero2:
    for contador in range (numero1,(numero2 +1)):
        print(contador)

else:    
    print("el numero 1 tiene que ser mas grande que el numero 2")