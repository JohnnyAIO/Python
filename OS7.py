import os
open("moribundo.txt", "w").close()
os.mkdir("vacio")
os.rmdir("vacio")
os.remove("moribundo.txt")
