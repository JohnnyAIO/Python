
nota = int(input("Ingrese su nota  "))

if(nota <= 0 or nota > 20):
    print ("Nota invalida")
elif (nota < 10):
    print ("Estudiante Reprobado")
elif(nota >= 10):
    print ("Estudiante Aprobado")
else:
    print ("Nota registrada")