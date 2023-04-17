import requests
import pytest

# Проверка что при запросе ключевых навыков по квери Тестирование статус код в ответе = 200
def test_check_status_code():
    response = requests.get('https://api.hh.ru/suggests/skill_set',
    params = {'text': 'Тестирование'})
    assert response.status_code == 200

# Проверяем что в выдаче по квери 'Функциональное тестирование' есть 'items' с конкретным номером 'id' и значением 'text'
def test_check_testing_1():
    response = requests.get('https://api.hh.ru/suggests/skill_set',
    params = {'text': 'Функциональное тестирование'})
    assert response.json()['items'] == [{'id': '3007', 'text': 'Функциональное тестирование'}]

# Проверяем что в выдаче по квери 'Функциональное тестирование' есть 'items' с конкретным номером 'id' и значением 'text'
def test_check_testing_2():
    response = requests.get('https://api.hh.ru/suggests/skill_set',
    params = {'text': 'Регрессионное тестирование'})
    assert response.json()['items'] == [{'id': '73592', 'text': 'Регрессионное тестирование'}]