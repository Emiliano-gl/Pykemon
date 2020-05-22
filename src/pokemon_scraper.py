from bs4 import BeautifulSoup
import requests
import json
from models.constants import *

url = 'https://pokemondb.net/pokedex/all'

page_response = requests.get(url, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

pokemonData = []
pokemonDict = {}

pokemonRows = page_content.find_all("tr")

for row in pokemonRows[1:]:
    statsHtml = row.find_all("td")[4:]
    typesHtml = row.find_all("a", attrs={"class": "type-icon"})
    name = row.find("a", attrs={"class": "ent-name"}).text
    megaHtml = row.find("small", attrs={"class": "text-muted"})

    statsArray = list(map(lambda data: int(data.text), statsHtml))
    typesArray = list(map(lambda data: TYPES.index(data.text), typesHtml))

    if megaHtml:
        name = megaHtml.text

    pokemonDict[name] = {
        "type1": typesArray[0],
        "hp": statsArray[0],
        "attack": statsArray[1],
        "defense": statsArray[2],
        "spattack": statsArray[3],
        "spdefense": statsArray[4],
        "speed": statsArray[5]
    }

    if len(typesArray) > 1:
        pokemonDict[name]["type2"] = typesArray[1]

file = open("../db/pokemons.json", "w")
file.write(json.dumps(pokemonDict))
file.close()

