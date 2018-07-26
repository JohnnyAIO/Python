#!/usr/bin/python
#Programa de prueba
class Persona:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
        print 'Se ha creado a: ', self.nombre , 'de ', self.edad , 'anos'

        def hablar(self, palabras):
        print self.nombre, ": ", palabras


        Jonathan = Persona()
        Jonathan.hablar("Hola, estoy hablando")
