with open ("Salario.txt", "r") as archivo
total_mes = 0
total_ingreso = 0
for linea in archivo.readlines():
        total_mes = total_mes + linea
        total_ingreso = total_ingreso + linea
    print("Mes: %d \n" % mes)
    print("Total de ganancias: %d$ " % total)
    archivo.write("Total de ganancias por los %d: %d$ \n" % (mes, total))
