import requests

token = '2c20cb7b04fbac2efd2ddef1d2c47973'
# Регистрируем тренера
response = requests.post('https://pokemonbattle.me:9104/trainers/reg', headers = {'Content-Type': 'application/json'},
               json = {'trainer_token': token, 'email': 'evgenyshandrik@mail.ru', 'password': 'Shandrik2023'})
print(response.text)

# Подтверждаем почту
response = requests.post('https://pokemonbattle.me:9104/trainers/confirm_email', headers = {'Content-Type': 'application/json'},
               json = {'trainer_token': token})
print(response.text)

# Добавляем покемона
add_pokemon_response = requests.post('https://pokemonbattle.me:9104/pokemons',
                                      headers = {'Content-Type': 'application/json', 'trainer_token': token},
               json = {"name": "Чубака", "photo": "https://dolnikov.ru/pokemons/albums/614.png"})
print(add_pokemon_response.text)

# Меняем имя созданного покемона на "Чуи" 
pokemon_name_change_response = requests.put('https://pokemonbattle.me:9104/pokemons',
                                      headers = {'Content-Type': 'application/json', 'trainer_token': token},
               json = {"pokemon_id": 6273, "name": "Чуи", "photo": "https://dolnikov.ru/pokemons/albums/614.png"})
print(pokemon_name_change_response.text)

# Ловим покемона в покебол
catch_pokemon_in_pokeball_response = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball',
                                      headers = {'Content-Type': 'application/json', 'trainer_token': token},
               json = {"pokemon_id": "6273"})
print(catch_pokemon_in_pokeball_response.text)