# Diccionarios anidados: Cajas dentro de cajas
colegio = {
    "001": {"nombre": "Edgar", "notas": {"matematicas": 20, "historia": 18}},
    "002": {"nombre": "Maria", "notas": {"matematicas": 15, "historia": 19}}
}
# Accediendo a un dato profundo
nota_math = colegio["002"]["notas"]["matematicas"]
print(f"La nota en matemáticas de 001 es: {nota_math}")
