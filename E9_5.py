with open("pares.txt", "r") as pares:
    with open("paresimpares.txt", "w") as archivo:
        L = pares.readlines()
        L.reverse()
        for i in L:
            archivo.write(i)
