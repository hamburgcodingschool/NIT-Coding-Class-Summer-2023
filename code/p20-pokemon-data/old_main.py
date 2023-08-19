import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=3")
data = response.json()

results = data["results"]

pokemonList = []

for pokemonShortInfo in results:
    print(pokemonShortInfo)
    response = requests.get(pokemonShortInfo["url"])
    data = response.json()

    print("ID: " + str(data["id"]))
    print("Name: " + data["name"])
    print("Height: " + str(data["height"]))
    print("Weight: " + str(data["weight"]))

    pokemonInfo = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }

    print(pokemonInfo)
    pokemonList.append(pokemonInfo)

print(pokemonList)

# pokemonList = [
#     {
#         "name": "Pikachu",
#         "id": 25,
#         "height": 45,
#         "weight": 34
#     },
#     {
#         "name": "Bulbasaur",
#         "id": 1,
#         "height": 45,
#         "weight": 34
#     },
# ]