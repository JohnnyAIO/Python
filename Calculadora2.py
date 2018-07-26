while True:
    a = int(input("Ingrese un valor: "))
    b = int(input("Ingrese un otro valor: "))
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("0) Salir")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 0:
        break
    elif opcion == 1:
        print(a + b)
    elif opcion == 2:
        print(a - b)
    elif opcion == 3:
        print(a * b)
    elif opcion == 4:
        print(a / b)
