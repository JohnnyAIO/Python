print("Universidad Central de Venezuela")
print("Facultad de Ciencias - Escuela de Computación")
print("Developer: Jonathan Torres C.I - 25.211.873")
print("Ejercicio 2")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese un ultimo numero: "))
if a > b:
    if a > c:
        print("El mayor es: %d (a)" % a)
        print("El medio es: %d (b)" % b) #correcto
        print("El menor es: %d (c)" % c)
        print(a, b, c)
    else:
        print("El mayor es: %d (c)" % c)
        print("El medio es: %d (a)" % a) #correcto
        print("El menor es: %d (b)" % b)
        print(c, a, b)
elif b > c:
    print("El mayor es: %d (b)" % b)
    print("El medio es: %d (c)" % c) #correcto
    print("El menor es: %d (a)" % a)
    print(b, c, a)
else:
    print("El mayor es: %d (c)" % c)
    print("El medio es: %d (b)" % b) #correcto
    print("El menor es: %d (a)" % a)
    print(c, b, a)
