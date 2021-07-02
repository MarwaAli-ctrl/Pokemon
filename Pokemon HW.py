#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/magnemite')
magnemite_data = r.get('https://pokeapi.co/api/v2/pokemon/magnemite')
if data.status_code == 200:
    magnemite_data = data.json()

    
magnemite = {
    'name' : magnemite_data['species']['name'],
    'abilities': [magnemite_data['abilities'][0]['ability']['name'],magnemite_data['abilities'][1]['ability']['name']],
    'weight' : magnemite_data['weight'], 
    'types' : [magnemite_data['types'][0]['type']['name'],magnemite_data['types'][1]['type']['name']]
}
print(magnemite)


import requests as r # often requests is imported under the alias r

data = r.get('https://pokeapi.co/api/v2/pokemon/bulbasaur')
data.status_code


if data.status_code == 200:
    bulbasaur_data = data.json()

bulbasaur = {
    'name' : bulbasaur_data['species']['name'],
    'abilities': [bulbasaur_data['abilities'][0]['ability']['name'],bulbasaur_data['abilities'][1]['ability']['name']],
    'weight' : bulbasaur_data['weight'], 
    'types' : [bulbasaur_data['types'][0]['type']['name'],bulbasaur_data['types'][1]['type']['name']]
}
print(bulbasaur)


data = r.get('https://pokeapi.co/api/v2/pokemon/74')
data.status_code

if data.status_code == 200:
    geodude_data = data.json()

geodude = {
    'name' : geodude_data['species']['name'],
    'abilities': [geodude_data['abilities'][0]['ability']['name'],geodude_data['abilities'][1]['ability']['name']],
    'weight' : geodude_data['weight'], 
    'types' : [geodude_data['types'][0]['type']['name'],geodude_data['types'][1]['type']['name']]
}
print(geodude)

data = r.get('https://pokeapi.co/api/v2/pokemon/4/')
data.status_code


if data.status_code == 200:
    charmander_data = data.json()


charmander = {
    'name' : charmander_data['species']['name'],
    'abilities': [charmander_data['abilities'][0]['ability']['name'],charmander_data['abilities'][1]['ability']['name']],
    'weight' : charmander_data['weight'], 
    'types' : [charmander_data['types'][0]['type']['name']]
}
print(charmander)




data = r.get('https://pokeapi.co/api/v2/pokemon/7/')
data.status_code


if data.status_code == 200:
    squirtle_data = data.json()


squirtle = {
    'name' : squirtle_data['species']['name'],
    'abilities': [squirtle_data['abilities'][0]['ability']['name'],squirtle_data['abilities'][1]['ability']['name']],
    'weight' : squirtle_data['weight'], 
    'types' : [squirtle_data['types'][0]['type']['name']]
}
print(squirtle)


data = r.get('https://pokeapi.co/api/v2/pokemon/19/')
data.status_code


if data.status_code == 200:
    rattata_data = data.json()


rattata = {
    'name' : rattata_data['species']['name'],
    'abilities': [rattata_data['abilities'][0]['ability']['name'],rattata_data['abilities'][1]['ability']['name']],
    'weight' : rattata_data['weight'], 
    'types' : [rattata_data['types'][0]['type']['name']]
}
print(rattata)


data = r.get('https://pokeapi.co/api/v2/pokemon/25/')
data.status_code


if data.status_code == 200:
    pikachu_data = data.json()


pikachu = {
    'name' : pikachu_data['species']['name'],
    'abilities': [pikachu_data['abilities'][0]['ability']['name'],pikachu_data['abilities'][1]['ability']['name']],
    'weight' : pikachu_data['weight'], 
    'types' : [pikachu_data['types'][0]['type']['name']]
}
print(pikachu)


data = r.get('https://pokeapi.co/api/v2/pokemon/158/')
data.status_code


if data.status_code == 200:
    totodile_data = data.json()


totodile = {
    'name' : totodile_data['species']['name'],
    'abilities': [totodile_data['abilities'][0]['ability']['name'],totodile_data['abilities'][1]['ability']['name']],
    'weight' : totodile_data['weight'], 
    'types' : [totodile_data['types'][0]['type']['name']]
}
print(totodile)

data = r.get('https://pokeapi.co/api/v2/pokemon/143/')
data.status_code


if data.status_code == 200:
    snorlax_data = data.json()


snorlax = {
    'name' : snorlax_data['species']['name'],
    'abilities': [snorlax_data['abilities'][0]['ability']['name'],snorlax_data['abilities'][1]['ability']['name']],
    'weight' : snorlax_data['weight'], 
    'types' : [snorlax_data['types'][0]['type']['name']]
}
print(snorlax)


data = r.get('https://pokeapi.co/api/v2/pokemon/163/')
data.status_code


if data.status_code == 200:
    hoothoot_data = data.json()


hoothoot = {
    'name' : hoothoot_data['species']['name'],
    'abilities': [hoothoot_data['abilities'][0]['ability']['name'],hoothoot_data['abilities'][1]['ability']['name']],
    'weight' : hoothoot_data['weight'], 
    'types' : [hoothoot_data['types'][0]['type']['name']]
}
print(hoothoot)


data = r.get('https://pokeapi.co/api/v2/pokemon/162/')
data.status_code


if data.status_code == 200:
    furret_data = data.json()


furret = {
    'name' : furret_data['species']['name'],
    'abilities': [furret_data['abilities'][0]['ability']['name'],furret_data['abilities'][1]['ability']['name']],
    'weight' : furret_data['weight'], 
    'types' : [furret_data['types'][0]['type']['name']]
}
print(furret)

data = r.get('https://pokeapi.co/api/v2/pokemon/8/')
data.status_code


if data.status_code == 200:
    sapphire_data = data.json()


sapphire = {
    'name' : sapphire_data['species']['name'],
    'abilities': [sapphire_data['abilities'][0]['ability']['name'],sapphire_data['abilities'][1]['ability']['name']],
    'weight' : sapphire_data['weight'], 
    'types' : [sapphire_data['types'][0]['type']['name']]
}
print(sapphire)


# In[ ]:





# In[ ]:




