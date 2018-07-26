lugares_vacios = [10,2,1,3,0]
while True:
    sala = int(input("Sala (0 Salir): "))
    if sala == 0:
        print("Fin")
        break
    if sala > len(lugares_vacios) or sala < 1:
        print("Sala invalida")
    elif lugares_vacios[sala-1] == 0:
        print("Disculpe, sala llena")
    else:
        lugares = int(input("Cuantos lugares desea usted (%d vacios):" % lugares_vacios[sala-1]))
        if lugares > lugares_vacios[sala-1]:
            print("Ese numero de lugares no esta disponible.")
        elif lugares < 0:
            print("Numero invalido")
        else:
            lugares_vacios[sala-1] -= lugares
            print("%d lugares vendidos" % lugares)
    print("Utilizacion de las salas")
    for x, l in enumerate(lugares_vacios):
        print("Sala %d - %d lugar(es) vacio(s)" % (x+1,l))
