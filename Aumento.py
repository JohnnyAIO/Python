salario = float(input("Ingrese su salario: "))
aumento = 0
if salario > 1250:
    aumento = salario + (salario*0.10)
    print("El salario aumentado es %6.2f" % (aumento))
else:
    aumento = salario + (salario*0.15)
    print("El salario aumentado es %6.2f" % (aumento))
