n = int(input("Ingrese un digito de 10 unidades: "))
x = 1
par = 0
impar = 0
while n > 0:
    y = n%10
    n = n//10
    w = y%2
    if w < 1:
        par = par + y
    else:
        impar = impar + y
    x = x+1
if x >= 10:
    print("Es un digito de 10 unidades")
    print("Total de la suma pares: %d" % par)
    print("Total de la suma de los impares: %d" % impar)
else:
    print("No es un digito de 10 unidades")
