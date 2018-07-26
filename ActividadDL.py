#!/usr/bin/env python
#Programa de prueba

frutas = input('Comes frutas? ')
if frutas == True:
    rangos = input('Cuantas veces a la semana comes frutas?')
    if rangos >= 5:
        print 'Sigue asi'
        dia = input('Cuantas frutas comes al dia')
        if dia >= 2:
            print 'Comes saludable'
        else:
            print 'Te recomiendo comer una fruta mas'
    elif 5 <= rangos and rangos >= 2:
        print 'Come mas fruta a la semana'
    elif rangos <= 2:
        print 'Necesitas comer mas frutas'
if frutas == False:
    print 'Necesitas comer frutas'
