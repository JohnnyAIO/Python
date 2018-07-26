stock = {"tomate": [ 1000, 2.30], #[0] = Cantidad, [1] = Precios
"lechuga": [500, 0.45],
"batata": [2001, 1.20],
"poroto": [100, 1.50]}
venta = input("Ingrese el nombre del producto a comprar: ")
total = 0
if venta in stock:
    compra = int(input("Ingrese la cantidad de compras: "))
    x = [[venta, compra]]
    print("Ventas:\n")
    for operacion in x:
        producto, cantidad = operacion
        if(stock[producto][0] < cantidad or cantidad < 0):
            print("No se puede comprar, exceso de mercancias")
        else:
            precio = stock[producto][1]
            costo = precio*cantidad
            print("%s: %3d x %6.2f = %6.2f" % (producto, cantidad, precio, costo))
            stock[producto][0] -= cantidad
            total += costo
else:
    print("El producto no existe")
print("Costo total: %21.2f \n" % total)
print("Stock:\n")
for clave, datos in stock.items():
    print("Descripcion: ", clave)
    print("Cantidad: ", datos[0])
    print("Precio: %6.2f\n" % datos[1])

