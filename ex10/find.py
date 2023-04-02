import requests

name = input("Entrez le nom du Pokémon: ")
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
if response.status_code == 404:
    print(f"Le Pokémon '{name}' n'a pas été trouvé")
else:
    pokemon = response.json()
    abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
    print(f"Le Pokémon {name} a les capacités suivantes :")
    for ability in abilities:
        print("- " + ability)
