from sys import argv
import subprocess
script = argv #python replicador.py
name = str(script[0])
print name
for i in range(0,10):
    directorio = 'dir'+str(i)
    subprocess.call(['mkdir',directorio])
    subprocess.call(['cp',name,directorio])
