primera = input("Digite una cadena: ")
segunda = input("Digite una segunda cadena: ")
tercera = ""
for letra in primera:
    if letra in segunda and letra not in tercera:
        tercera += letra
if tercera == "":
    print("Cadenas comunes no encontradas")
else:
    print("Caracteres en comunes: %s" % tercera)
