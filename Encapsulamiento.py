#!/usr/bin/python
#Programa de prueba
class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print 'Se ha creado a: ', self.nombre , 'de ', self.edad , 'anos'

        def hablar(self, *palabras):
            for frases in palabras:
                print self.nombre, ": ", frases

class Deportista(Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte = deporte
        print 'Se ha creado a: ', self.nombre , 'de ', self.edad , 'anos'

    def placticarDeporte(self):
        print self.nombre, ": Voy a practicar"
#Metodos Privados - Encapsulados
    def verMiDeporte(self):
        return .__deporte;

Juan = Persona(30, "Juan")
Juan.hablar("Hola estoy hablando", "Estoy yo")
Luis = Deportista(18, "Luis", "Natacion")
Luis.hablar("Hola, estoy hablando", "Este soy yo")
Luis.placticarDeporte()
print "Practico: ", Luis.verMiDeporte()
