import mysqlService
import httpFetchService

pokemonList = httpFetchService.getAllPokemonList()

current = 0
for pokemonInfo in pokemonList:
    current += 1
    print(f"Saving: {current}/{len(pokemonList)}")
    mysqlService.insertPokemon(pokemonInfo)
