L = [15, 7, 27, 39]
p = int(input("Digite un valor a buscar: "))
y = int(input("Digite un valor a buscar: "))
t = 0
x = 0 # contador para p
z = 0 # contador para y
while t < len(L):
    if L[t] == p:
        x = t
        t += 1
    elif L[t] == y:
        z = t
        t += 1
    else:
        t += 1
if  x < z:
    print("El valor primer que se encontro fue %d de la posicion %d" % (p, x))
    print("El valor segundo que se encontro fue %d de la posicion %d" % (y, z))
else:
    print("El valor primer que se encontro fue %d de la posicion %d" % (y, z))
    print("El valor segundo que se encontro fue %d de la posicion %d" % (p, x))
