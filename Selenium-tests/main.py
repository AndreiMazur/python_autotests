import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '655286d35f9dec473fc4945582880e77'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
body_reg = {
    "trainer_token": TOKEN,
    "email": "mazur.andreimazur@yandex.ru",
    "password": "Salut!9Mai",
    "password_re": "Salut!9Mai"
}
body_confirmation= {
    "trainer_token": TOKEN
}

body_create= {
    "name": "generate",
    "photo_id": -1
}
body_rename= {
    "pokemon_id": "366951",
    "name": "New Name",
    "photo_id": 481
}
body_catch= {
    "pokemon_id": "309350"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_reg)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_create.text)

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_create.text)

message = response_create.json()['message']
print(message)