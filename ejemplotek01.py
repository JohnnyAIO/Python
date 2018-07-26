#!/usr/bin/python
#Programa de prueba

from Tkinter import*

class interfaz:
    def __init__(self,contenedor):
        self.e1 = Label(contenedor, text = "Etiqueta 1", fg = "Black", bg = "white")
        self.e2 = Label(contenedor, text = "Etiqueta 2", fg = "Black", bg = "gray")
        self.e3 = Label(contenedor, text = "Etiqueta 3", fg = "Black", bg = "green")

        self.e1.pack (side = TOP)
        self.e2.pack (side = RIGHT)
        self.e3.pack (side = BOTTOM, fill = X)

ventana = Tk()
minterfaz = interfaz(ventana)
ventana.mainloop()
