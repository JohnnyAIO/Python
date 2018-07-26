#!/usr/bin/python
#Programa de prueba

from Tkinter import*

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta 1", fg = "Black", bg = "white")

        self.e1.place (x = 20, y = 30, width =120, height = 25)


ventana = Tk()
minterfaz = interfaz(ventana)
ventana.mainloop()
