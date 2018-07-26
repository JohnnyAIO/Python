ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print("\n Existen %d clientes en la fila" % len(fila))
    print("Fila actual:", fila)
    print("Digite F para adicionar un cliente al final de la fila")
    print("A para atender, S para salir.")
    operacion = input("Operacion (F, A o S):")
    x = 0
    salir = False
    while x < len(operacion):
        if operacion[x] == "A":
            if(len(fila))>0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
                x = x+1
            else:
                print("Fila vacia, nadie para atender")
        elif operacion[x] == "F":
            ultimo += 1
            fila.append(ultimo)
            x = x+1
        elif operacion[x] == "S":
            salir = True
            break
        else:
            print("Operacion invalida, Digite A, F o S")
            x = x+1
    if(salir):
        break
