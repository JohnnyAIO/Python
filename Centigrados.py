c = int(input("Ingrese la temperatura en centigrados"))
f = (9*c/5) + 32
print("Total de Farenheit: %d " % f)

auto = int(input("Ingrese la cantidad de km recorridos "))
dias = int(input("Ingrese la cantidad de dias obtenidos "))
#6obs.f por dia alquilado el auto
#0,15bs.f por km alquilado del auto
auto_t = auto*0.15
dias_t = dias*60
total = auto_t + dias_t
print("Total de dias alquilados : %5.2f " % dias_t)
print("Total de recorridos : %5.2f " % auto_t)
print("Total por gastar : %d " % total)

