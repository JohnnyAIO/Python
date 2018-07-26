categoria = int(input("Ingrese la categoria: "))
if categoria == 1:
    precio = 10
elif categoria == 2:
    precio = 18
elif categoria == 3:
    precio = 23
elif categoria == 4:
    precio = 26
elif categoria == 5:
    precio = 31
else:
    print("Categoria invalida, digite un valor entre 1 y 5")
    precio = 0
print("El precio del producto es: %.2f" % precio)
