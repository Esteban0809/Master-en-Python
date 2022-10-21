import re


class Coche :
    #Atributos o propiedades(variables)
    #caracteristicas del coche
    color = "Rojo"
    marca =" Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje =  500
    plazas = 2

    def __init__(self,color, marca, modelo, velocidad, caballaje, plazas ) :
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

        soy_publico = " Hola,  soy un atributo publico"
        __soy_privado = "Hola, soy un atributo privado"

    # Metodos son acciones que hace el objeto(funciones)
    def getPrivado(self):
        return self.__Soy_privado
    def setColor(self, color):
        self.color = color

    def getColor (self):
        return self.color

    def setModelo (self, modelo):
        self.modelo = modelo
    
    def getModelo (self):
        return self.modelo

    def setMarca (self, marca):
        return self.marca 

    def getMarca (self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar (self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):

        info = "--------------- INFORMACIÓN DEL COCHE---------------------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca :" +str (self.getMarca())
        info += "\n Modelo :" + self.getModelo()
        info += "\n Velocidad :" +str( self.getVelocidad())

        return info
        