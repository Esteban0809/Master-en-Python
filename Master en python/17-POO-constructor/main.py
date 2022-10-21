from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xyara", 100, 180, 4)
carro3 = Coche("rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getInfo())
print(carro2.getInfo())
print(carro1.getInfo())
print(carro3.getInfo())

# Dectectar tipado
carro3 = "aleatorio"
if type(carro3)== Coche:
    print("es un objeto correcto!!")
else:
    print("No es un objeto")

# Visibilidad
#print(carro.soy_publico)
print(carro.getPrivado())
