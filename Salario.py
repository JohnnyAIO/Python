import sys
total = 0
with open ("Salario.txt", "a") as archivo:
    money = int(sys.argv[1])
    horas = int(sys.argv[2])
    dias = int(sys.argv[3])
    mes = int(sys.argv[4])
    total = total + money*horas*dias*mes
    archivo.write("Mes: %d \n" % mes)
    archivo.write("Total de ganancias: %d$ \n" % total)
    print("Mes: %d \n" % mes)
    print("Total de ganancias: %d$ " % total)
    total_mes = 0
    total_ingreso = 0
    for linea in archivo.readlines():
        total_mes = total_mes + linea
        total_ingreso = total_ingreso + linea
    print("Mes: %d \n" % mes)
    print("Total de ganancias: %d$ " % total)
    archivo.write("Total de ganancias por los %d: %d$ \n" % (mes, total))
    

    
