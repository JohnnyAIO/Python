import sys
import os
import os.path as ruta
import urllib.request

mascara = "'margin: 5px 0px 5 px %dpx'"
def generar_estilo(nivel):
    return mascara % (nivel*20)

def generar_listado(pagina, directorio):
    nraiz = ruta.abspath(directorio).count(os.sep)
    for raiz, directorios, archivos in os.walk(directorio):
        nivel = raiz.count(os.sep) - nraiz
        pagina.write("<p style=%s> %s </p>" % (generar_estilo(nivel), raiz))
        estilo = generar_estilo(nivel+1)
        for a in archivos:
            camino_completo = ruta.join(raiz, a)
            tamaño = ruta.getsize(camino_completo)
            link = urllib.request.pathname2url(camino_completo)
            pagina.write("<p style=%s> <a href='%s'> %s </a> (%d bytes)</p>" % (estilo, link, a ,tamaño))

if len(sys.argv) < 2:
    print("Digite un directorio")
    sys.exit(1)

directorio = sys.argv[1]

pagina = open("archivos.html","w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Arquivos</title>
</head>
<body>
""")
pagina.write("Archivos encontrados a partir del directorio: %s" % directorio)
generar_listado(pagina, directorio)
pagina.write("""
</body>
</html>
""")
pagina.close()
