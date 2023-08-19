import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1010")
data = response.json()

results = data["results"]

pokemonList = []

current = 0
for pokemonShortInfo in results:
    current += 1
    total = len(results)
    percentage = round(current / total * 100)
    # print(f"Loading: {current}/{total}: {percentage}%")
    if current % 20 == 0:
        print(f"Loading: {percentage}%")

    response = requests.get(pokemonShortInfo["url"])
    data = response.json()

    pokemonInfo = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"]
    }
    pokemonList.append(pokemonInfo)

tallestPokemon = pokemonList[0]
shortestPokemon = pokemonList[0]
heaviestPokemon = pokemonList[0]
lightestPokemon = pokemonList[0]

totalHeight = 0
totalWeight = 0

for pokemonInfo in pokemonList:
    totalHeight += pokemonInfo["height"]
    totalWeight += pokemonInfo["weight"]

    if pokemonInfo["height"] > tallestPokemon["height"]:
        tallestPokemon = pokemonInfo
    if pokemonInfo["height"] < shortestPokemon["height"]:
        shortestPokemon = pokemonInfo

    if pokemonInfo["weight"] > heaviestPokemon["weight"]:
        heaviestPokemon = pokemonInfo
    if pokemonInfo["weight"] < lightestPokemon["weight"]:
        lightestPokemon = pokemonInfo

avgHeight = totalHeight / len(pokemonList)
avgWeight = totalWeight / len(pokemonList)

print(f"The total height of all Pokemons is {totalHeight}")
print(f"The average height of all Pokemons is {avgHeight}")

print(f"The total weight of all Pokemons is {totalWeight}")
print(f"The average weight of all Pokemons is {avgWeight}")

print(f"The tallest pokemon is id {tallestPokemon['id']} with the name {tallestPokemon['name']}")
print(f"The shortest pokemon is id {shortestPokemon['id']} with the name {shortestPokemon['name']}")
print(f"The heaviest pokemon is id {heaviestPokemon['id']} with the name {heaviestPokemon['name']}")
print(f"The lightest pokemon is id {lightestPokemon['id']} with the name {lightestPokemon['name']}")
