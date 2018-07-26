casa = float(input("Ingrese el precio a comprar: "))
salario = float(input("Ingrese el salario: "))
tiempo = int(input("Ingrese el año a pagar: "))
cuota = (casa*tiempo)/salario
descuento = salario * 0.30
if cuota > descuento:
    print("Lo sentimos no podra adquirir la casa debido a un alto cuota")
    print("Total de la cuota %6.2f$ mensual por %d años" % (cuota, tiempo))
else:
    print("Ha sido aprobado tu peticion")
    print("Total de la cuota %6.2f$ mensual por %d años" % (cuota, tiempo))
