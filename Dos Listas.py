primera = []
segunda = []
while True:
    n = int(input("Ingrese un numero: (0 para Salir): "))
    if n == 0:
        break
    primera.append(n)
while True:
    n = int(input("Ingrese un numero: (0 para Salir): "))
    if n == 0:
        break
    segunda.append(n)
tercera = primera[:]
tercera.extend(segunda)
x = 0
while x < len(tercera):
    print("%d: %d" % (x, tercera[x]))
    x += 1
