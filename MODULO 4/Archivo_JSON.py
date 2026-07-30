import json

usuario = {"nombre": "Edgar", "habilidades": ["Python", "Git", "API"]}

# Guardar un diccionario como JSON (dump)
with open("perfil.json", "w") as f:
    json.dump(usuario, f)

# Leer un JSON (load)
with open("perfil.json", "r") as f:
    data = json.load(f)
    print(f"Usuario cargado: {data['nombre']}")
