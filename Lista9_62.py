ANCHO = 79
with open("entrada.txt", "r") as entrada:
    for linea in entrada.readlines():
        if linea[0] == ";":
            continue
        elif linea[0]==">":
            print(linea[1:].rjust(ANCHO))
        elif linea[0]=="*":
            print(linea[1:].center(ANCHO))
        else:
            print(linea)

