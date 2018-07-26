n = int(input("Ingrese la deuda inicial: "))
interes = int(input("Ingrese los intereses: "))
paga = int(input("Ingrese el valor mensual: "))
x = 1
total = 0
while x <= 24:
    acum =  n*interes/100
    total = total + acum - paga
    x = x+1
    #print("%5.2f" % total)
print("El ingreso inicial %d de sus intereses %d son: %5.2f" % (n, interes, total))
