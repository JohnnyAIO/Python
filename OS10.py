import os.path
import os
if os.path.exists("z"):
    print("El directorio z existe.")
else:
    print("El directorio z no-existe.")
    os.mkdir("z")
