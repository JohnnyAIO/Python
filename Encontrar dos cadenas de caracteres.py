s = input("Ingrese una cadena de caracteres: ")
x = input("Ingrese la letra a buscar: ")
p = 0
while p > -1:
    p = s.find(x, p)
    if p >= 0:
        print("%s encontrado en la posicion: %d de %s" % (x, p, s))
        p += 1
