#!/usr/bin/python
#Programa de prueba

pi = 3.141516
l1 = ["Numero", "Letra",[23,pi,278],"variable"]
l2 = ["Cesar", "Octavio", "Mario"]
print "Buscar el indice de la lista -variable-"
print l1.index("variable")

print "\n"
print "Agregar un elemento en la ultima lista"
print l1.append("constante")

print "\n"
print "Contar veces que aparece el valor -variable-"
print l1.count("variable")
print "\n"

print "Insetar un valor en el indice seleccionado"
l1.insert(2, "Valor Nuevo")
print l1
print "\n"
print "Agregar una lista a una cadena"
l1.extend(l2)
print l1

print "\n"
l1.pop(2)
print "Eliminar el valor del indice seleccionado"
print l1
print "\n"
l1 = ["Letra", "Numero", "Variable", "Incognita"]
l1.remove("Numero")
print "Lista nueva sin el numero"
print l1

print "\n"
l1 = ["Numero", "Letra",[23,pi,278],"variable"]
print "Invirtiendo el orden de la lista"
l1.reverse()
print l1
