import sys
def verifica_pagina(nombre, linea, pagina):
    if(linea == Lineas):
        rodar = "= %s - Pagina: %d =" % (nombre_archivo, pagina)
        archivo.write(rodar.center(Laro-1)+"\n")
        pagina += 1
        linea = 1
    return linea, pagina

def escribir(archivo, linea, nlineas, pagina):
    archivo.write(linea+"\n")
    return verifica_pagina(archivo, nlineas+1, pagina)

if len(sys.argv)!=4:
    print("\n Uso del archivo para largo, paginas y lineas")
    sys.exit(1)
nombre_archivo = int(sys.argv[1])
Largo = int(sys.argv[2])
Lineas = int(sys.argv[3])

entrada = open(nombre_archivo, encoding="utf-8")
salida = open("Salida_pagina.txt", "w", encoding="utf-8")
pagina = 1
lineas = 1

for linea in entrada.readlines():
    palabras = linea.rstrip().split(" ")
    linea = ""
    for p in palabras:
        p = p.strip()
        if len(linea)+len(p)+1>Largo:
            lineas, pagina=escribir(salida, linea, lineas, pagina)
            linea = ""
        linea += p+" "
    if(linea != ""):
        lineas, pagina=escribir(salida, linea, lineas, pagina)

while(lineas != 1):
    lineas, pagina=escribir(salida, "", lineas, pagina)
entrada.close()
salida.close()
