palabras = ["casa", "bola", "ucv", "computacion", "manguera", "jonathan", "supremo"]
indice = int(input("Digite un numero: "))
palabra = palabras[(indice*776) % len(palabras)]
print(palabra)
for x in range(100):
    print()
digitadas = []
aciertos = []
errores = 0
while True:
    contrasena=""
    for letra in palabra:
        contrasena += letra if letra in aciertos else "."
    print(contrasena)
    if contrasena == palabra:
        print("Usted acerto :D")
        break
    intento = input("\n Digite una letra: ").lower().strip()
    if intento in digitadas:
        print("!Usted ya intento esta letra¡")
        continue
    else:
        digitadas += intento
        if intento in palabra:
            aciertos += intento
        else:
            errores += 1
            print("!usted erro¡")
    print("X==:==\nX : ")
    print("X  O " if errores >= 1 else "X")
    linea2 = ""
    if errores == 2:
        linea2 = "  |  "
    elif errores == 3:
        linea2 = "\ | "
    elif errores >= 4:
        linea2 = "\ | /"
    print("X%s" % linea2)
    linea3 = ""
    if errores == 5:
        linea3 += " / "
    elif errores >= 6:
        linea3 += "/   \ "
        
    print("X%s" % linea3)
    print("X\n=================")
    if errores == 6:
        print("¡Ahorcado!")
        print("La palabra secreta era: %s" % palabra)
        break
