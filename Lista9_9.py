Lista = ["ejemplo.txt", "Saludos.txt", "ejercicio1.txt"]
#x = 0
#while (x < 3):
#    with open(Lista[x], "r") as archivo:
#        for l in archivo.readlines():
#            print(l)
#    x += 1
with open("guardar.txt", "w") as guardar:
    for archivos in Lista:
        print(open(archivos).readlines())
        x = archivos.readlines()
        guardar.write(x)
