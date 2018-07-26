print("Universidad Central de Venezuela")
print("Facultad de Ciencias - Escuela de Computación")
print("Developer: Jonathan Torres C.I - 25.211.873")
print("Ejercicio 1")
n = int(input("Ingrese la cantidad de datos a procesar: "))
if n < 0:
    print("Numero invalido, debe ser positivo")
x = 1
acum = 0
while x <= n:
    y = int(input("Ingrese el dato %d: " % x))
    acum = acum + y
    x += 1
prom = y/n
print("De %d datos su promedio es: %d" % (x-1, prom))
    
