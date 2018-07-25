archivo = open("pareseimpares.txt", "w")
pares = open("pares.txt")
impares = open("impares.txt")
for n in pares.readlines():
    for p in impares.readlines():
        if int(p) < int(n):
            archivo.write(n)
        else:
            archivo.write(p)
impares.close()
pares.close()
archivo.close()
