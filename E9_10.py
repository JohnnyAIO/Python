import sys

if len(sys.argv)<2:
    print("\n Cantidad de parametros invalidos")
    sys.exit(1)

salida = open("Salida_unica.txt", "w", encoding="utf-8")
for nome in sys.argv[1:]:
    archivo = open(nome, "r", encoding="utf-8")
    for linea in archivo:
        salida.write(linea)
    archivo.close()
salida.close()
