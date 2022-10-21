"""
Eercicio 3. escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primero numeros 
naturales. Resolver con for y con while. 


#while



while contador <= 60:

    cuadrado = contador*contador
    print(f" El cuadrado de  {contador} es {cuadrado}")

    contador+=1
"""
    #FOR

for numero in range (61):
    cuadrado = numero*numero
    print(f"el cuadrado de {numero} es {cuadrado}")