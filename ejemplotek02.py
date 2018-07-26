#!/usr/bin/python
#Programa de prueba

from Tkinter import*

class interfaz:
    def __init__(self,contenedor):
        self.textoE3 = StringVar()
        self.e1 = Label(contenedor, text = "Convertir Celisus a Farenheit", fg = "Black")
        self.e2 = Label(contenedor, text = "Celius", fg = "Black")
        self.e3 = Label(contenedor, text = "Farenheit", fg = "Black")
        self.e4 = Button(contenedor, text = "Convertir", fg = "Black", bg = "cyan", command =self.hacerConversion)
        self.e5 = Entry(contenedor, fg = "Black", bg = "white")
        self.e6 = Label(contenedor, text = "", fg = "Black", textvariable = self.textoE3)

        self.e1.grid (column = 0, row = 0, columnspan = 2)
        self.e2.grid (column = 0, row = 1)
        self.e3.grid (column = 0, row = 2)
        self.e4.grid (column = 0, row = 3, columnspan = 2)
        self.e5.grid (column = 1, row = 1)
        self.e6.grid (column = 1, row = 2)

        def hacerConversion(self):
            cel = float(self.e5.get())
            far = (cel*1,8)+32
            self.textoE3.set(far)

ventana = Tk()
minterfaz = interfaz(ventana)
ventana.mainloop()
