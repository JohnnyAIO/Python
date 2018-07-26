n = int(input("Ingrese un ano bisiesto: "))
if(n%4 == 0 or n%400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
