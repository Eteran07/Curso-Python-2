import requests # type: ignore

# Endpoint de ejemplo (PokeAPI)
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = respuesta.json()

print(f"El peso de Pikachu es: {data['weight']}")
