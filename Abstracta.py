#!/usr/bin/python
#Programa de prueba
from abc import ABCMeta, abstractmethod
class Persona:
    __metaclass__=ABCMeta
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print 'Se ha creado a: ', self.nombre , 'de ', self.edad , 'anos'
        @abstractmethod
        def hablar(self, *palabras):pass

class Deportista(Persona):
    def __init__(self, edad, nombre, deporte):
        self.edad = edad
        self.nombre = nombre
        self.deporte = deporte
        print 'Se ha creado a: ', self.nombre , 'de ', self.edad , 'anos'

    def placticarDeporte(self):
        print self.nombre, ": Voy a practicar"

    def hablar(self, *palabras):
        for frases in palabras:
            print self.nombre, ": ", frases

Luis = Deportista(18, "Luis", "Natacion")
Luis.hablar("Hola, estoy hablando", "Este soy yo")
Luis.placticarDeporte()
