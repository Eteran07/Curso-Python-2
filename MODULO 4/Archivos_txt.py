# Escribir en un .txt (w = write)
with open("diario.txt", "w") as archivo:
    archivo.write("Hoy aprendi a manejar archivos en Python.")

# Leer un .txt (r = read)
with open("diario.txt", "r") as archivo:
    contenido = archivo.read()
    print(f"Lo que guardamos fue: {contenido}")