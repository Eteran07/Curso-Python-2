clave = ""
intentos = 0

while clave != "1234":
    # El for cuenta los intentos del 1 al 3
    for i in range(3):
        clave = input("Ingresa la clave: ")
        
        if clave == "1234":
            print("Acceso concedido")
            break
        else:
            intentos = intentos + 1
            print("Intento fallido")
            
    # Si ya falló 3 veces, rompe el while para cerrar
    if intentos == 3:
        break

if intentos == 3:
    print("Acceso invalido")
