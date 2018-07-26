stock = {"tomate": [1000, 2.30],
         "lechuga": [500, 0.45],
         "batata": [2001, 1.20],
         "poroto": [100, 1.50]}
total = 0
print("Ventas: \n")
while True:
    producto = input("Digite el nombre del producto, fin para terminar:")
    if producto == "fin":
        break
    if producto in stock:
        cantidad = int(input("Cantidad: "))
        if cantidad <= stock[producto][0]:
            precio = stock[producto][1]
            costo = precio * cantidad
            print("%12s: %3d x %6.2f = %6.2f" % (producto, cantidad, precio, costo))
            stock[producto][0] -= cantidad
            total += costo
        else:
            print("Cantidad no solicitada")
    else:
        print("Nombre del producto invalido")
print("Costo total: %21.2f \n" % total)
print("Stock: \n")
for clave, datos in stock.items():
    print("Descripcion: ", clave)
    print("Cantidad: ", datos[0])
    print("Precio: %6.2f\n" % datos[1])
