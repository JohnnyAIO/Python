s = input("Ingrese una letra: ")
n = s.lower()
if((int(n)) < 0 or (int(n)) >= 0):
    print("Es un digito")
elif( n == "a" or n == "e" or n == "i" or n == "o" or n == "u"):
    print("Es una vocal")
else:
    print("Es una consonante")

