"""
Ejercico 3. Programa que compruebe so una variableestá vacia
y si está vacia rellenarla con texto en minusculas y mostrarlo en mayusculas.
"""
# Mostrar el texto
texto = ""

if len(texto.strip()) <= 0:

    texto = " hola soy un texto en minusculas"
    print(texto.upper())



else:
    print(f"La variable tiene contenido{texto}")