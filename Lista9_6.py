ANCHO = 79
with open("entrada.txt", "r") as entrada:
    for linea in entrada.readlines():
        if linea[0] == ";":
            continue
            for n in range(1, 41):
                print("=")
        elif linea[0]==">":
            #startwiths = leer la cadena de texto para String
            print(linea[1:].rjust(ANCHO))
            for n in range(1, 41):
                print("=")
        elif linea[0]=="*":
            print(linea[1:].center(ANCHO))
            for n in range(1, 41):
                print("=")
        else:
            print(linea)

