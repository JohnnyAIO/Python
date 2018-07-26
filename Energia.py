tipo = input("Ingrese el tipo de Instalacion, R = residencias, I = Industrias, C = Comercios")
consumo = int(input("Ingrese la cantidad de energia consumida: "))
if tipo == "R":
    if consumo < 500:
        total = 0.40
    else:
        total = 0.65
elif tipo == "I":
    if consumo < 1000:
        total = 0.55
    else:
        total = 0.60
elif tipo == "C":
    if consumo < 5000:
        total = 0.55
    else:
        total = 0.60
else:
    print("Lo siento, opcion invalida")
energia = consumo * total
print("Total del costo es %6.2f" % energia)
