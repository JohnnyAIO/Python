import sys

if len(sys.argv)!=2:
    print("Parametros invalidos")
    sys.exit(1)

nombre = sys.argv[1]
contador = {}
fila = 1
columnna = 1
archivo = open(nombre, "r", encoding="utf-8")
for linea in archivo:
    linea = linea.strip().lower()
    palabras = linea.split(" ")
    for p in palabras:
        if p == "":
            columnna += 1
            continue
        if p in contador:
            contador[p].append((fila, columnna))
        else:
            contador[p] = [(fila, columnna)]
        columnna += len(p)+1
    fila += 1
    columnna += 1
archivo.close()

for clave in contador:
    print("%s = %d" % (clave,contador[clave]))
