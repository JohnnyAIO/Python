Horas=float(input())
Minutos=float(input())
print(str(Horas)+" "+str(Minutos))
Min_Reloj=Minutos*5/60
Min_Horas=Horas*5
Diff=Min_Horas-Minutos+Min_Reloj
Grados=Diff*6
Grados=(360+Grados)%360
print("El resultado es: "+str(Grados))