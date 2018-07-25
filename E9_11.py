import sys

if len(sys.argv)!=2:
    print("Parametros invalidos")
    sys.exit(1)

nombre = sys.argv[1]
contador = {}

archivo = open(nombre, "r", encoding="utf-8")
for linea in archivo:
    linea = linea.strip().lower()
    palabras = linea.split()
    for p in palabras:
        if p in contador:
            contador[p]+=1
        else:
            contador[p]=1
archivo.close()

for clave in contador:
    print("%s = %d" % (clave,contador[clave]))
