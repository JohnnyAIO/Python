ultimo = 10
fila1 = []
fila2 = []
while True:
    print("\n Existen %d clientes en la fila 1 y %d clientes en la fila 2." % (len(fila1), len(fila2)))
    print("Fila 1 actual:", fila1)
    print("Fila 2 actual:", fila2)
    print("Digite F para adicionar un cliente en la fila 1 (G para fila 2)")
    print("A para despachar a fila 1 (B para fila 2)")
    print("S para salir")
    operacion = input("Operacion (F,G,A,B o S): ")
    x = 0
    salir = False
    while x < len(operacion):
        if operacion[x] == "A" or operacion[x] == "F":
            fila = fila1
            x += 1
        else:
            fila = fila2
            x += 1
        if operacion[x] == "A" or operacion[x] == "B":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print("Cliente %d atentido" % atendido)
                x += 1
            else:
                print("Fila vacia, Ningun cliente por atender")
                x += 1
        elif operacion[x] == "F" or operacion[x] == "G":
            ultimo += 1
            fila.append(ultimo)
            x += 1
        elif operacion[x] == "S":
            salir = True
            break
        else:
            print("Operacion invalida, opciones viables (F, G, A, B o S)")
            x += 1
    if(salir):
        brek
