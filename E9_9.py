import sys

if len(sys.argv)<2:
    print("Cantidad de parametros invalidos")
    sys.exit(1)

for nome in sys.argv[1:]:
    archivo = open(nome, "r")
    for linea in archivo:
        print(linea, end="")
    archivo.close()
