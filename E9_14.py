nombre = "entrada.txt"
inicio = 5
final = 9
with open(nombre, "r") as archivo:
    for linea in archivo.readlines()[inicio+2:final]:
        print(linea)


#Entrada.txt
            
#Esta linea no debe ser impresa

#Esta linea debe ser impresa alineada a la derecha

#Esta linea debe ser centrada

#Una linea normal

#Otra linea

