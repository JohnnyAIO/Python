tabla = { "Lechuga" : 1.25,
          "Tomate" : 0.23,
          "Cebolla" : 3.23,
          "Mango" : 2.34,
          "Papa" : 4.00,
          "Platano" : 1.23 }
while True:
    producto = input("Digite el nombre del producto para eliminar, fin para terminar:")
    if producto == "fin":
        break
    if producto in tabla:
        print("Se elimino: ")
        print(tabla.pop(producto))
    else:
        print("¡Producto no encontrado!")
