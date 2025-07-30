import requests
import pytest
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '655286d35f9dec473fc4945582880e77'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 37567

def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_response_have_name():
    response_get = requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'ralts'

@pytest.mark.parametrize('key, value', [('name', 'ralts'),('trainer_id', '37567'),('id','366951')])
def test_parametrize(key, value):
       response_parametrize = requests.get(url= f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
       assert response_parametrize.json()['data'][0][key] == value

def test_trainer_info():
    response_info = requests.get(url= f'{URL}/trainers/', params={'trainer_id': TRAINER_ID})
    assert response_info.status_code == 200
    assert response_info.json()['data'][0]['trainer_name'] == 'Andrei'