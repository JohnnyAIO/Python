import sys
print("Numero de parametros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print("Parametro %d = %s" % (n,p))
