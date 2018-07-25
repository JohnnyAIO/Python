import sys
for n in sys.argv:
     archivo = open("ejercicio1.txt", "w")
     archivo.write(n)
     archivo2 = open("ejercicio2.txt", "w")
     archivo2.write(n)
archivo.open()
archivo2.open()
