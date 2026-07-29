#1. Operadores Aritméticos 
precio_base = 50.00
impuesto = 12.50
precio_total = precio_base + impuesto # Resultado: 62.50
descuento = 10.00
precio_final = precio_total - descuento # Resultado: 52.50




#2. Operadores Relacionales 
edad_usuario = 18
edad_minima = 18
es_mayor = edad_usuario >= edad_minima # Resultado: Verdadero




#3. Operadores Lógicos y Toma de Decisiones  Ejemplo con Operador Y (AND): && o and

tiene_entrada = True
es_mayor_de_edad = True

# La computadora toma la decisión
if tiene_entrada and es_mayor_de_edad:
    print("¡Puedes ingresar al evento!")
else:
    print("Acceso denegado.")
