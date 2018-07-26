Fila = 5
Columna = "E"
BL = input()
Fila_Blanca = int(BL[0])
Columnna_Blanca = BL[1]
Tipo_Blanca = BL[3:5]

NE = input()
Fila_Negra = int(NE[0])
Columnna_Negra = NE[1]
Tipo_Negra = NE[3:5]

Pos = input()

if Columnna_Blanca != "A" and Columnna_Blanca != "B" and Columnna_Blanca != "C" and Columnna_Blanca != "D" and Columnna_Blanca != "E":
    print("Entrada Invalida")
elif Columnna_Negra != "A" and Columnna_Negra != "B" and Columnna_Negra != "C" and Columnna_Negra != "D" and Columnna_Negra != "E":
    print("Entrada Invalida")
if Fila_Blanca > Fila or Fila_Blanca < 1 or Fila_Negra > Fila or Fila_Negra < 1:
    print("Entrada Invalida")
if Columnna_Blanca == "A":
    Columnna_Blanca = 1
elif Columnna_Blanca == "B":
    Columnna_Blanca = 2
elif Columnna_Blanca == "C":
    Columnna_Blanca = 3
elif Columnna_Blanca == "D":
    Columnna_Blanca = 4
elif Columnna_Blanca == "E":
    Columnna_Blanca = 5
if Columnna_Negra == "A":
    Columnna_Negra = 1
elif Columnna_Negra == "B":
    Columnna_Negra = 2
elif Columnna_Negra == "C":
    Columnna_Negra = 3
elif Columnna_Negra == "D":
    Columnna_Negra = 4
elif Columnna_Negra == "E":
    Columnna_Negra = 5
## En caso del Peon
if(Tipo_Negra == "PE" or Tipo_Blanca == "PE"):
    if Pos == "NE":
        if Tipo_Negra == "PE":
            if Columnna_Negra+1 == Columnna_Blanca and Fila_Negra+1 == Fila_Blanca:
                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha Blanca del [%s]" % (NE[0:2], BL[0:2]))
            elif Columnna_Negra-1 == Columnna_Blanca and Fila_Negra+1 == Fila_Blanca:
                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha Blanca del [%s]" % (NE[0:2], BL[0:2]))
            elif Columnna_Negra == Columnna_Blanca or Fila_Negra == Fila_Blanca:
                print("Sin perdidas")
            else:
                print("Imposible")
    else:
        if Tipo_Blanca == "PE":
            if Columnna_Blanca-1 == Columnna_Negra and Fila_Blanca-1 == Fila_Negra:
                print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
            elif Columnna_Blanca+1 == Columnna_Negra and Fila_Blanca-1 == Fila_Negra:
                print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
            elif Columnna_Blanca == Columnna_Negra or Fila_Blanca == Fila_Negra:
                print("Sin perdidas")
            else:
                print("Imposible")
if(Tipo_Negra == "TE" or Tipo_Blanca == "TE"):
    ## En caso de las Torres
    if Pos == "NE":
        if Tipo_Negra == "TE":
            if Columnna_Negra == Columnna_Blanca or Fila_Negra == Fila_Blanca:
                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
            else:
                print("Sin perdidas")
    else:
        if Tipo_Blanca == "TE":
            if Columnna_Blanca == Columnna_Negra or Fila_Blanca == Fila_Negra:
                print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha negra del [%s]" % (BL[0:2], NE[0:2]))
            else:
                print("Sin perdidas")
                
if(Tipo_Negra == "CA" or Tipo_Blanca == "CA"):
    ## En caso del Caballo
    if Pos == "NE":
        if(Fila_Negra+1 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        else:
            if(Fila_Negra+1 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca):
                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
            else:
                if(Fila_Negra+2 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                else:
                    if(Fila_Negra+2 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca):
                        print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                    else:
                        if(Fila_Negra-2 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca):
                            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                        else:
                            if(Fila_Negra-2 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca):
                                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                            else:
                                if(Fila_Negra-1 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca):
                                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                                else:
                                    if(Fila_Negra-1 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca):
                                        print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                                    else:
                                        print("Sin perdidas")
    elif Pos == "BL":
        if(Fila_Blanca+1 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        else:
            if(Fila_Blanca-1 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra):
                print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
            else:
                if(Fila_Blanca+2 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra):
                    print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                else:
                    if(Fila_Blanca+2 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra):
                        print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                    else:
                        if(Fila_Blanca-2 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra):
                            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                        else:
                            if(Fila_Blanca-2 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra):
                                print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                            else:
                                if(Fila_Blanca-1 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra):
                                    print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                                else:
                                    if(Fila_Blanca-1 == Fila_Negra and Columnna_Blanca-2 == Columnna_Negra):
                                        print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                                    else:
                                        print("Sin Perdidas")
    else:
        print("Sin perdidas")
if(Tipo_Negra == "AL" or Tipo_Blanca == "AL"):
    ## En caso de los Alfines
    if Pos == "NE":
        if((Fila_Negra+1 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca) or (Fila_Negra+2 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca)
           or (Fila_Negra+3 == Fila_Blanca and Columnna_Negra+3 == Columnna_Blanca) or (Fila_Negra+4 == Fila_Blanca and Columnna_Negra+4 == Columnna_Blanca)):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        elif((Fila_Negra+1 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca) or (Fila_Negra+2 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca)
            or (Fila_Negra+3 == Fila_Blanca and Columnna_Negra-3 == Columnna_Blanca) or(Fila_Negra+4 == Fila_Blanca and Columnna_Negra-4 == Columnna_Blanca)):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        elif((Fila_Negra-1 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca) or (Fila_Negra-2 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca) 
            or (Fila_Negra-3 == Fila_Blanca and Columnna_Negra+3 == Columnna_Blanca) or (Fila_Negra-4 == Fila_Blanca and Columnna_Negra+4 == Columnna_Blanca)):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        elif((Fila_Negra-1 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca) or (Fila_Negra-2 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca)
            or (Fila_Negra-3 == Fila_Blanca and Columnna_Negra-3 == Columnna_Blanca) or (Fila_Negra-4 == Fila_Blanca and Columnna_Negra-4 == Columnna_Blanca)):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        else:
            print("Sin perdidas")
    elif Pos == "BL":
        if((Fila_Blanca+1 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra) or (Fila_Blanca+2 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra)
           or (Fila_Blanca+3 == Fila_Negra and Columnna_Blanca+3 == Columnna_Negra) or (Fila_Blanca+4 == Fila_Negra and Columnna_Blanca+4 == Columnna_Negra)):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif((Fila_Blanca+1 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra) or (Fila_Blanca+2 == Fila_Negra and Columnna_Blanca-2 == Columnna_Negra)
            or (Fila_Blanca+3 == Fila_Negra and Columnna_Blanca-3) or (Fila_Blanca+4 == Fila_Negra and Columnna_Blanca-4 == Columnna_Negra)):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif((Fila_Blanca-1 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra) or (Fila_Blanca-2 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra) or (Fila_Blanca-3 == Fila_Negra and Columnna_Blanca+3 == Columnna_Negra)
             or (Fila_Blanca-4 == Fila_Negra and Columnna_Blanca+4 == Columnna_Negra)):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif((Fila_Blanca-1 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra) or (Fila_Blanca-2 == Fila_Negra and Columnna_Blanca-2 == Columnna_Negra) or (Fila_Blanca-3 == Fila_Negra and Columnna_Blanca-3 == Columnna_Negra)                 or (Fila_Blanca-4 == Fila_Negra and Columnna_Blanca-4 == Columnna_Negra)):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        else:
            print("Sin Perdidas")
    else:
        print("Sin Perdidas")        
if(Tipo_Blanca == "RX" or Tipo_Negra == "RX"):
    ##En caso de la Reyna
    if Pos == "NE":
        ##Movimiento de las Torres
        if(Fila_Negra == Fila_Blanca or Columnna_Negra == Columnna_Blanca):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        else:
            if Pos == "NE":
                if((Fila_Negra+1 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca) or (Fila_Negra+2 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca)
                or (Fila_Negra+3 == Fila_Blanca and Columnna_Negra+3 == Columnna_Blanca) or (Fila_Negra+4 == Fila_Blanca and Columnna_Negra+4 == Columnna_Blanca)):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                elif((Fila_Negra+1 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca) or (Fila_Negra+2 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca)
                or (Fila_Negra+3 == Fila_Blanca and Columnna_Negra-3 == Columnna_Blanca) or(Fila_Negra+4 == Fila_Blanca and Columnna_Negra-4 == Columnna_Blanca)):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                elif((Fila_Negra-1 == Fila_Blanca and Columnna_Negra+1 == Columnna_Blanca) or (Fila_Negra-2 == Fila_Blanca and Columnna_Negra+2 == Columnna_Blanca)
                or (Fila_Negra-3 == Fila_Blanca and Columnna_Negra+3 == Columnna_Blanca) or (Fila_Negra-4 == Fila_Blanca and Columnna_Negra+4 == Columnna_Blanca)):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                elif((Fila_Negra-1 == Fila_Blanca and Columnna_Negra-1 == Columnna_Blanca) or (Fila_Negra-2 == Fila_Blanca and Columnna_Negra-2 == Columnna_Blanca)
                or (Fila_Negra-3 == Fila_Blanca and Columnna_Negra-3 == Columnna_Blanca) or (Fila_Negra-4 == Fila_Blanca and Columnna_Negra-4 == Columnna_Blanca)):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                else:                        
                    print("Sin perdidas")
            elif Pos == "BL":
                  if((Fila_Blanca+1 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra) or (Fila_Blanca+2 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra)
                  or (Fila_Blanca+3 == Fila_Negra and Columnna_Blanca+3 == Columnna_Negra) or (Fila_Blanca+4 == Fila_Negra and Columnna_Blanca+4 == Columnna_Negra)):
                      print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                  elif((Fila_Blanca+1 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra) or (Fila_Blanca+2 == Fila_Negra and Columnna_Blanca-2 == Columnna_Negra)
                  or (Fila_Blanca+3 == Fila_Negra and Columnna_Blanca-3) or (Fila_Blanca+4 == Fila_Negra and Columnna_Blanca-4 == Columnna_Negra)):
                      print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                  elif((Fila_Blanca-1 == Fila_Negra and Columnna_Blanca+1 == Columnna_Negra) or (Fila_Blanca-2 == Fila_Negra and Columnna_Blanca+2 == Columnna_Negra) or (Fila_Blanca-3 == Fila_Negra and Columnna_Blanca+3 == Columnna_Negra)
                  or (Fila_Blanca-4 == Fila_Negra and Columnna_Blanca+4 == Columnna_Negra)):
                      print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                  elif((Fila_Blanca-1 == Fila_Negra and Columnna_Blanca-1 == Columnna_Negra) or (Fila_Blanca-2 == Fila_Negra and Columnna_Blanca-2 == Columnna_Negra) or (Fila_Blanca-3 == Fila_Negra and Columnna_Blanca-3 == Columnna_Negra)
                  or (Fila_Blanca-4 == Fila_Negra and Columnna_Blanca-4 == Columnna_Negra)):
                      print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
                  else:
                      print("Sin Perdidas")
if(Tipo_Blanca == "RE" or Tipo_Negra == "RE"):
    #Movimiento deL Rey
    if Pos == "NE":
        if(Columnna_Negra + 1 == Columnna_Blanca or Columnna_Negra - 1 == Columnna_Blanca):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        elif(Fila_Negra + 1 == Fila_Blanca or Fila_Negra - 1 == Fila_Blanca):
            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
        else:
            if(Fila_Negra - 1 == Fila_Blanca and Columnna_Negra + 1 == Columnna_Blanca):
                print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
            else:
                if(Fila_Negra - 1 == Fila_Blanca and Columnna_Negra - 1 == Columnna_Blanca):
                    print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                else:
                    if(Fila_Negra + 1 == Fila_Blanca and Columnna_Negra + 1 == Columnna_Blanca):
                      print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                    else:
                        if(Fila_Negra + 1 == Fila_Blanca and Columnna_Negra - 1 == Columnna_Blanca):
                            print("La ficha Negra ubicada en la posicion [%s] logra alcanzar a la ficha blanca del [%s]" % (NE[0:2], BL[0:2]))
                        else:
                            print("Sin perdidas")
    elif Pos == "BL":
        if(Columnna_Blanca + 1 == Columnna_Negra or Columnna_Blanca - 1 == Columnna_Negra):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif(Fila_Blanca + 1 == Fila_Negra or Fila_Blanca - 1 == Fila_Negra):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif(Fila_Blanca + 1 == Fila_Negra and Columnna_Blanca + 1 == Columnna_Negra or Fila_Blanca + 1 == Fila_Negra and Columnna_Blanca - 1 == Columnna_Negra):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        elif(Fila_Blanca - 1 == Fila_Negra and Columnna_Blanca + 1 == Columnna_Negra or Fila_Blanca - 1 == Fila_Negra and Columnna_Blanca - 1 == Columnna_Negra):
            print("La ficha Blanca ubicada en la posicion [%s] logra alcanzar a la ficha Negra del [%s]" % (BL[0:2], NE[0:2]))
        else:
            print("Sin perdidas")
    else:
        print("Sin Perdidas")