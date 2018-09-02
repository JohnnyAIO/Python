contador = {}
fila = 1
columnna = 1
with open("entrada.txt", "r") as archivo:
    for linea in archivo.readlines():
        palabras = linea.split()
        print(linea)
        for p in palabras:
            if p == "":
                columnna += 1
                continue
            if p in contador:
                contador[p].append((fila, columnna))
            else:
                contador[p] = [(fila, columnna)]
            columnna += len(p)
            fila += 1
            columnna = 1
for clave in contador:
    print("%s = %s" % (clave, contador[clave]))
