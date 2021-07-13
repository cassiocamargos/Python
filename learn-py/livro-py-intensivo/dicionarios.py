######DICIONARIOS######

#Criando lista vazia e adc pares chave-valor
'''cars={}
cars['color'] = 'green'
cars['points'] = 5
print(cars)
del cars ['points'] #deleta par chave-valor
print(cars)
cars['color'] = 'blue' #muda par chave-valor
print("a cor mudou para " + cars['color'] + '.')'''

'''#Percorrendo todos os pares-chave com um laço
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

#Percorrendo todas as chaves de um dicionário com um laço
print('\n')
for name in favorite_languages.keys():
    print(name.title())

#Encontra uma determinada chave (usando o if)
print('\n')
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends: 
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

print('\n')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Percorrendo as chaves de um dicionário em ordem usando um laço - função sorted() ordena a lista antes de percorrê-la
print('\n')
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")'''

'''favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print('\t' + language.title())

#Quando colocamos set() em torno de uma lista que contenha itens duplicados, Python identifica os itens únicos na lista e cria um conjunto a partir desses itens.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())'''

'''######DICIONARIO EM UMA LISTA######
# Cria uma lista vazia para armazenar alienígenas
aliens = []

# Cria 30 alienígenas verdes
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Modifica os três primeiros alienigenas 
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Mostra todos os aliens
for alien in aliens[:]:
    print(alien)

# Mostra os 5 primeiros alienígenas
for alien in aliens[0:5]:
    print(alien)
print("...")
#Mostra o ultimo alienigena
for alien in aliens[-1:]:
    print(alien)
# Mostra quantos alienígenas foram criados
print("Total number of aliens: " + str(len(aliens)))'''

"""######LISTA EM UM DICIONARIO######
'''# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())"""

'''######DICIONARIO EM UM DICIONARIO######
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())'''


responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


