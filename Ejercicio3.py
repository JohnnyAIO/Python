m = int(input("Ingrese la cantidad de metros: "))
mili = m*1000
print("De metros %d a Milimetros son: %d " % (m, mili))

d = int(input("Introduce la cantidad de dias: "))
h = d*24 
mi = 60*d
sec = 60*mi
print("Total de segundo es: %d " % sec)

salario = int(input("Ingrese el salario minimo: "))
aumento = int(input("Ingrese el aumento en porcentaje: "))
total = salario + (salario*aumento/100)
print("El aumento del salario es: %d " % total)

mercancia = int(input("Ingrese el costo de la mercancia: "))
descuento = int(input("Ingrese el descuento: "))
total = mercancia - (mercancia*descuento/100))
print("El total del descuento del producto es: " % total)



