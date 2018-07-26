while True:
    valor = float(input("Digite el valor a pagar: "))
    if valor == 0.00:
        break
    billetes = 0
    actual = 100
    apagar = valor
    while True:
	    if actual <= apagar:
		    apagar -= actual
		    billetes += 1
	    else:
		    if actual >= 1:
				print("%d billetes de %d$" % (billetes, actual))
		    else:
			    print("%d monedas de %5.2f$" % (billetes, actual))
		    if apagar < 0.01:
			    break
		    if actual == 100:
			    actual = 50
		    elif actual == 50:
			    actual = 20
		    elif actual == 20:
			    actual = 10
		    elif actual == 10:
			    actual = 5
	  	    elif actual == 5:
			    actual = 1
		    elif actual == 1:
			    actual = 0.50
		    elif actual == 0.50:
			    actual = 0.10
		    elif actual == 0.10:
			    actual = 0.05
		    elif actual == 0.05:
			    actual = 0.02
		    elif actual == 0.02:
			    actual = 0.01
		    billetes = 0
