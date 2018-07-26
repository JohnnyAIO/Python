primera = input("Ingrese una cadena: ")
segunda = input("Ingrese otra cadena: ")
tercera = ""
for letras in primera:
    if letras not in segunda:
        tercera += letras
if tercera == "":
    print("Toda la cadena ha sido eliminada")
else:
    print("Cadena generada: %s" % tercera)
