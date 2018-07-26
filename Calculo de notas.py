notas = []
x = 0
suma = 0
while True:
    n = int(input("Ingrese la nota %d: " % (x+1)))
    if n == 0:
            break
    notas.append(n)
    x += 1
x = 0
while x < len(notas):
    print("Nota %d: %d" % (x, notas[x]))
    suma += notas[x]
    x += 1
print("Promedio es: %5.2f" % (suma/x))
