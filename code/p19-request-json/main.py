import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()

print(data["weight"])

# print(data["results"][24]["name"])
#
# print("======")
#
# for pokemon in data["results"]:
#     print(pokemon["name"])
