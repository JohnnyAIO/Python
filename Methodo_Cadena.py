#!/usr/bin/python
#Programa de prueba

cadena1 = "La Violencia es el ultimo recurso del incompetente"
print "Contador de veces la letra e"
print cadena1.count("e")
print cadena1.count("Violencia")

print "Minuscula toda la oracion"
print cadena1.lower()

print "Mayuscula toda la oracion"
print cadena1.upper()

print "Cambiar las palabras recurso - medio"
print cadena1.replace("recurso","medio",1)

print "Organizar sub-cadenas"
print cadena1.split("o",2)

print "Buscar el valor y devolver su indice"
print cadena1.find("v")

print "Buscar el valor y devolver su indice"
print cadena1.rfind("i")

print "Imprimir los elementos con Turpia"
l1 = ["J", "0", "N", "A"," T", "H", "A", "N"]
v = "-"
print v.join(l1)
