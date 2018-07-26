#!/usr/bin/python
#Programa de prueba

import sqlite3

def insertar():
    db1 = sqlite3.connect('novelas.db')
    print "Esta en la fase de insercion de datos"
    nombre1 = raw_input("Escribe el titulo de la novela/libro  ")
    autor1 = raw_input("Escribe el autor  ")
    year1 = str(input("Escribe el ano de publicacion  "))
    consulta = db1.cursor()

    strConsulta = "INSERT INTO tabla (nombre, autor, year) values ("+nombre1+","+autor1+","+year1+");"
    print(strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()

insertar()
