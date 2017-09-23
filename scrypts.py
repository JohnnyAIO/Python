#!/usr/bin/python
from sys import argv
script, filename = argv

print "Creando el archivo %r "%filename

file = open(filename, 'w')
file.write("Programador el que lo lea :V ")
file.close()
print "terminado"
