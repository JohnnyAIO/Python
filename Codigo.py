acum = 0
while True:
    v = int(input("Introduce el codigo de barras: "))
    if v == 1:
        precio = 0.50
    elif v == 2:
        precio = 1.00
    elif v == 3:
        precio = 4.00
    elif v == 5:
        precio = 7.00
    elif v == 9:
        precio = 8.00
    elif v == 0:
        break
    acum = acum + precio
print("Total de productos son %5.2f" % acum)
