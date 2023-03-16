import requests
import pytest

# Проверка что при запросе тренеров статус код в ответе = 200
def test_check_status_code():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

# Проверяем что в выдаче по квери с id тренера есть тренер с конкретным именем
def test_check_trainer_name():
    response = requests.get('https://pokemonbattle.me:9104/trainers',
    params = {'trainer_id': 3415})
    assert response.json()['trainer_name'] == 'Майк Вазовский'