L = [3,2,1,5,4]
fin = 5
while fin > 1:
    cambio = False
    x = 0
    while x < (fin - 1):
        if L[x] < L[x+1]:
            cambio = True
            temp = L[x]
            L[x] = L[x+1]
            L[x+1] = temp
        x+=1
    if not cambio:
        break
    fin -= 1
for e in L:
    print(e)
