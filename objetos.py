#!/usr/bin/python
class Humano:
    habilidad  ="inteligente"
    nombre = "Jonathan"
    def nombrar(self,n):
        self.nombre = n
persona = Humano()
persona.nombrar("Jonathan")

print "Hay un muchacho llamado %s y es demasiado %s"%(Humano.nombre,Humano.habilidad)
