categoria = int(input("Digite la categoria del producto: "))
if categoria == 1:
    precio = 10
else:
    if categoria == 2:
        precio = 18
    else:
        if categoria == 3:
            precio = 23
        else:
            if categoria == 4:
                precio = 26
            else:
                if categoria == 5:
                    precio = 31
                else:
                    print("Categoria invalida, digite un valor entre 1 y 5")
                    precio = 0
print("El precio del producto es: %6.2f$" % precio)
