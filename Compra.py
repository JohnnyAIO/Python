gastos = 0
compra = 0
i = 0
producto = int(input("Ingrese la cantidad de productos a comprar"))
while(i <= producto):
    nombre = (input("Ingrese el nombre del producto  "))
    compra = int(input("Ingrese el precio del: %s  " % (nombre)))
    gastos = gastos + compra
    compra = compra + compra
    i = i+1
print("Total de Inversion es: %d" % (compra))
