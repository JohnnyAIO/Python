#!/usr/bin/python
#Programa de prueba

#Calculadora de Areas
F = 3,141516
def areacuadrado():
    lado = input("Cual es el valor del lado \n")
    x = lado**2
    print "\n El area del cuadrado es: ", x, " Unidades cuadradas"

#Area del Triangulo
def areatriaungulo():
    base=input("Ingrese el valor de la base \n")
    altura = input("Ingrese el valor de la altura \n")
    y=(base*altura)/2
    print "\n El area del Trinangulo es: ", y, " Unidades cuadradas"

#Area del Circulo
def acirculo():
    radio=input("Ingrese el valor del radio \n")
    z=(F*radio)**2
    print "\n El area del circulo es:  ",z, " Unidades cuadradas"

    i=True
    while i==True:
        print "\n Menu de Calculadora de Figuras Geometricas Python"
        area=input("\n Elige la figura para calcular su area \n 1) Cuadrado \n 2) Tringualo \n 3) Circulo")
        if area==1:
            areacuadrado()
        elif area==2:
            areatriaungulo()
        elif area==3:
            acirculo()
        else:
            print "Ingresa una opcion valida"
            i=input("\n Quieres calcular otra area \n True or False?")
