import sys
import os
import os.path as ruta
import math

def tamaño_humanos(tamaño):
    if tamaño == 0:
        return "0 Byte"
    grandeza = math.log(tamaño, 10)
    if grandeza < 3:
        return "%d bytes" % tamaño
    elif grandeza < 6:
        return "%7.3f KB" % (tamaño / 1024.0)
    elif grandeza < 9:
        return "%f MB" % (tamaño / pow(1024,2))
    elif grandeza < 12:
        return "%f GB" % (tamaño / pow(1024,3))

mascara_estilo = "'margin: 5px 0px 5px %dpx;'"

def genera_estilo(nivel):
    return mascara_estilo % (nivel*30)

def generar_nivel_estilo(raiz):
    def nivel(camino):
        xnivel = camino.count(os.sep) - nraiz
        return genera_estilo(xnivel)
    nraiz = raiz.count(os.sep)
    return nivel
def generar_lista(pagina,directorio):
    directorio = ruta.abspath(directorio)
    identificador = generar_nivel_estilo(directorio)
    pila = [ [directorio, 0] ]
    for raiz, directorios, archivos in os.walk(directorio):
        while not raiz.startswith(pila[-1][0]):
            ultimo = pila.pop()
            pagina.write("<p style=%s> %s </p>" % (identificador(ultimo[0])))
            pila[-1][1] += ultimo[1]
        pagina.write("<p style=%s> %s </p>" % (identificador(raiz), raiz)
        d_tamaño = 0
        for a in archivos:
                     camino_completo = ruta.join(raiz, a)
                     d_tamaño += ruta.getsize(camino_completo)
        pila.append( [raiz, d_tamaño])
    while len(pila) > 1:
                     ultimo = pila.pop()
                     pagina.write("<p style=%s> %s </p>" % (identificador(ultimo[0])))
                     pila[-1][1] += ultimo[1]

if len(sys.argv)<2:
    print("Digite un nombre del directorio")
    sys.exit(1)

directorio = sys.argv[1]

pagina = open("t_archivos.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Archivos</title>
</head>
<body>
""")
pagina.write("Archivos encontrados en el directorio: %s" % diretório)
generar_lista(pagina, directorio)
pagina.write("""
</body>
</html>
""")
pagina.close()
