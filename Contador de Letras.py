frase = input("Digite una frase para contar las letras: ")
d = {}
for letras in frase:
    if letras in d:
        d[letras] = d[letras] + 1
    else:
        d[letras] = 1
print(d)
