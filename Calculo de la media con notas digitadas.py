notas = [0,0,0,0,0]
suma = 0
x = 0
while x < 5:
    notas[x] = float(input("Nota %d:" % x))
    suma += notas[x]
    x += 1
x = 0
while x < 5:
    print("Nota %d: %6.2f" % (x, notas[x]))
    x += 1
print("Media: %5.2f" % (suma/x))

    
