agenda = []
cambio = False
uso = " Defecto "
def pide_nombre(comp=""):
    nombre = input("Nombre: ")
    if nombre == "":
        nombre = comp
    return(nombre)
def pide_telefono(comp=""):
    telefono = input("Telefono: ")
    if telefono == "":
        telefono = comp
    return(telefono)
def pide_cedula():
    return(int(input("Ingrese su cedula: ")))
def muestra_datos(nombre, telefono, cedula):#Escribir los archivos
    print("Nombre: {} Telefono: {} Cedula: {}".format(nombre,telefono,cedula))
def pide_nombre_archivo():#Nombre achivo -> Guardar Informacion
    return(input("Nombre del archivo: "))
def investigacion(nombre):
    mnombre = nombre.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnombre:#Campo Nombre
            return p
    return None
def nuevo():
    global agenda, cambio
    nombre = pide_nombre()
    if investigacion(nombre) != None:
        print("Lo sentimos el nombre existe")
        return
    telefono = pide_telefono()
    cedula = pide_cedula()
    agenda.append([nombre, telefono, cedula])
    agenda.sort()
    cambio = True
def borra():
    global agenda, cambio
    nombre = pide_nombre()
    p = investigacion(nombre)
    if p != None:
        x = comprobar()
        if x:
            del agenda[p]
            cambio = True
    else:
        print("Nombre no encontrado.")
def comprobar():
    n = int(input("Desea realizar esta operacion? 1: Si, 2: No -> "))
    if n == 1:
        return True
def altera():
    global cambio
    p = investigacion(pide_nombre())
    if p != None:
        nombre = agenda[p][0]
        telefono = agenda[p][1]
        cedula = agenda[p][2]
        print("Encontrado: ")
        muestra_datos(nombre, telefono, cedula)
        x = comprobar()
        if (x):
            nombre = pide_nombre()
            telefono = pide_telefono()
            cedula = pide_cedula()
            agenda[p] = [nombre, telefono, cedula]
            cambio = True
    else:
        print("Nombre no encontrado.")
def lista():
    print("\nAgenda\n\n------")
    x = 1
    for e in agenda:
        print("%d)" % x, end="")
        muestra_datos(e[0], e[1], e[2]) #Nombre Telefono Cedula
        print("-------\n")
        x = x+1
def lee():
    global agenda, cambio, uso
    if (cambio):
        print("No has guardado los cambios en el archivo, desea guardar?")
        x = comprobar()
        if(x):
            graba()
    nombre_archivo = pide_nombre_archivo()
    uso = nombre_archivo
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    agenda = []
    for l in archivo.readlines(): # JONATHAN 5772359 25211873 Jesus#
        nombre, telefono, cedula = l.strip().split(" ")
        agenda.append([nombre, telefono, cedula]) #Numero -> Caracteres
    agenda.sort() #Aqui aplica
    cambio = False
    archivo.close()
    
    
def graba():
    global uso
    nombre_archivo = pide_nombre_archivo()
    uso = nombre_archivo
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    for e in agenda:
        archivo.write("{} {} {}\n".format(e[0],e[1],e[2]))
    archivo.close()
                      
def valida_franja_entero(pregunta, inicio, fin):
    while True:        
        try:
            valor = int(input(pregunta))
            if inicio <= valor <= fin:
                return(valor)
        except ValueError:
            print("Valor invalido, por favor digitar entre {} y {}".format(inicio,fin))
def menú():
    print("""
1 - Nuevo
2 - Altera
3 - Borra
4 - Lista
5 - Graba
6 - Lee
0 - Salir
""")
    print("Archivo utilizando actualmente: %s" % uso)
    print("Tamaño de la agenda: %d Dato Cambiado: %s" % (len(agenda), cambio))
    return valida_franja_entero("Elección una opción: ",0,6)

while True:
    opción = menú()
    if opción == 0:
        break
    elif opción == 1:
        nuevo()
    elif opción == 2:
        altera()
    elif opción == 3:
        borra()
    elif opción == 4:
        lista()
    elif opción == 5:
        graba()
    elif opción == 6:
        lee()
                      
        
