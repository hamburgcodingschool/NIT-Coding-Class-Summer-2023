import requests

def getAllPokemonURLs():
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000")
    data = response.json()

    return data["results"]

def getAllPokemonList():
    results = getAllPokemonURLs()

    pokemonList = []
    current = 0
    for pokemonShortInfo in results:
        current += 1
        if current % 20 == 0:
            percentage = round(current / len(results) * 100)
            print(f"Loading: {percentage}%")

        response = requests.get(pokemonShortInfo["url"])
        data = response.json()

        pokemonInfo = {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "image": data["sprites"]["other"]["official-artwork"]["front_default"]
        }
        pokemonList.append(pokemonInfo)

    return pokemonList