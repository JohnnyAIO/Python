import os
import os.path as camino
nombre = input("Ingrese el nombre a buscar:  ")
if camino.isdir(nombre):
    print("Es una carpeta")
elif camino.isfile(nombre):
    print("Es un archivo")
else:
    print("La data no existe")
