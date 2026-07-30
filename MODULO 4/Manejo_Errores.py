# Ejemplo robusto: Pedir datos hasta que sean correctos
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break # Rompe el ciclo si el dato es correcto
    except ValueError:
        print("¡Error! Eso no es un número. Intenta de nuevo.")

print(f"¡Perfecto! Tienes {edad} años.")