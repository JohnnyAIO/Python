distancia = float(input("Ingrese la distancia que deseas recorrer: "))
impuesto = 0
if distancia <= 200:
    impuesto = impuesto + (distancia*0.50)
    print("En total de %6.2fkm para recorrer son: %6.2f$" % (distancia, impuesto))
else:
   impuesto = impuesto + (distancia*0.45)
   print("En total de %6.2fkm para recorrer son: %6.2f$" % (distancia, impuesto)) 
