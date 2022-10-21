"""
ejercico 8. ¿ cuanto es el X por ciento de X numero?
                    20% de 150


"""
numero = int (input(" Introduce el numero:"))
porcentaje = int(input(f"¿ que porcentaje quieres sacar de {numero: }  :"))

operacion = ( numero *(porcentaje/100))
print(f"el {porcentaje} % de {numero} es: {operacion}")


