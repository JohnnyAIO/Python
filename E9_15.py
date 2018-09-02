import sys
import random

palabras = []
clave = {}

def cargar_palabras():#Escribir en el programa, directorios
	archivo = open("palabras.txt", "r", encoding = "utf-8")
	for palabra in archivo.readlines():
		palabra = palabra.strip().lower()
		if palabra != "":
			palabras.append(palabra)
	archivo.close()

def cargar_clave():
	archivo = open("clave.txt", "r", encoding="utf-8")
	for linea in archivo.readlines():
		linea in linea.strip()
		if linea != "":
			usuario, contador = linea.split(";")
			clave[usuario] = int(contador)
	archivo.close()

def guardar_clave():#Escribir en el archivo
	archivo = open("clave.txt", "w", encoding="utf-8")
	for usuario in clave.keys():
		archivo.write("%s;%d\n" % (usuario, clave[usuario]))
	archivo.close()

def actualizar_clave():
	if nombre in clave:
		clave[nombre] += 1
	else:
		clave[nombre] = 1
	guardar_clave()

def escribir_clave():
	clave_ordenado = []
	for usuario, score in clave.items():
		clave_ordenado.append([usuario, score])
	clave_ordenado.sort(key = lambda score: score[1])
	print("\n\n Mejores jugadores por numero de aciertos:")
	clave_ordenado.reverse()
	for up in clave_ordenado:
		print("%30s %10d" % (up[0], up[1]))


cargar_clave()
cargar_palabras()

palabra = palabras[random.randint(0,len(palabras)-1)]

digitadas = []
aciertos = []
errores = 0
while True:
        x = ""
	for letra in palabra:
		x += letra
		if letra in aciertos:
                        continue
		else:
                        "."
                print(x)
                if x == palabra:
                        print("Acertaste :D")
                        nombre = input("Digite su nombre")
                        actualizar_clave(nombre)
                        break
                tentativa = input("\n Digite una letra:").lower().strip()
                if tentativa in digitadas:
                        print("Ya utilizaste esta letra")
                        continue
                else:
                        digitadas += tentativa
                        if tentativa in palabra:
                                aciertos += tentativa
                        else:
                                errores += 1
                                print("Error!")
        print("X==:==\nX  : ")
        print("X  O ")
        if errores >= 1:
                continue
        else:
                "X"
        linea2 = ""
            if errores == 2:
                linea2 = "  |   "
            elif errores == 3:
                linea2 = " \|   "
            elif errores >= 4:
                linea2 = " \|/ "
        print("X%s" % linea2)
        linea3 = ""
            if errores == 5:
                linea3 += " /     "
            elif errores >= 6:
                linea3 += " / \ "
        print("X%s" % linea3)
        print("X\n===========")
            if errores == 6:
                print("Ahorcado!")
                break
        escribir_clave()
