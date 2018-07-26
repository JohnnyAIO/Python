cadena = input("Ingrese una cadena: ")
contador = {}
for letra in cadena:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1
for clave in contador:
    print("%s: %dx" % (clave, contador[clave]))

#cadena = input("Ingrese una cadena: ")
#for letra in cadena:
 #   x = cadena.count(letra)
  #  print(x)

