L = [40, 30, 20, 10]
p = int(input("Digite un numero a buscar: "))
for x in L:
    if x == p:
        print("%d encontrado " % x)
        break
else:
    print("No encontrado")

## While -> Todo va dentro
## For -> Puede ir afuera o adentro
