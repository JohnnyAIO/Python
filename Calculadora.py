a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Ingrese una opcion 1) Sumar, 2) Restar, 3) Multiplicar, 4) Dividir :"))
total = 0
if c == 1:
    total = total + a+b
elif c == 2:
    total = total + a-b
elif c == 3:
    total = total + a*b
elif c == 4 :
    total = total + a/b
else:
    print("Lo siento opcion invalida, las viables son 1 - 4")
print("El resultado de la operacion es: %d" % total)
