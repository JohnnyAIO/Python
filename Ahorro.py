n = int(input("Ingrese el deposito inicial: "))
interes = int(input("Ingrese los intereses: "))
x = 1
total = 0
while x <= 24:
    acum =  n*interes/100
    total = total + acum
    x = x+1
    #print("%5.2f" % total)
print("El ingreso inicial %d de sus intereses %d son: %5.2f" % (n, interes, total))
