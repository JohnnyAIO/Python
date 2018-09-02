import sys
import os
import os.path as camino
import urllib.request


if len(sys.argv) < 2:
    print("Digite un nombre o directorio para recolectar archivos jpg e png")
    sys.exit(1)

directorio = sys.argv[1]

pagina = open("imagenes.html", "w", encoding = "utf-8")
pagina.write("""
<!DOCTYPE html>
<html>
<head>
meta charset="utf-8">
<title> Páginas mostradas </title>
</head>
<body>
""")
pagina.write("Imagenes encontradas : %s" % directorio)
for entrada in os.listdir(directorio):
    nombre, extension = camino.splitext(entada)
    if extension in [".jpg", ".png"]:
        ruta_completo = camino.join(directorio, entrada)
        link = urllib.request.pathname2url(ruta_completo)
        pagina.write("<p><a href='%s'>%s</a></p>" % (link,entrada))

pagina.write("""
</body>
</html>
""")
