"""
Ejercicio 10 : el programa tiene que pedir la nota de 15 alumnos
y tiene que sacar por pantalla cuantos han aprobado y cauntos han suspendido.
"""
contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes? : "))

while contador <=  numero_alumnos:
     nota = int(input(f"¿ que nota quires ponerle al \"alumno? {contador} :"))

    if nota >= 5:
         aprobados += 1
    else:
        suspendidos += 1

     contador += 1
     
     print(f"\nAlumnos suspendidos : {suspendidos}")
     print(f"\nAlumnos aprobados : {aprobados}"))

