"""def hi():
    ###Exibe uma saudação simples
    print('hello!')
hi()"""


'''def greet_user(username):
    ###Exibe uma saudação simples.
    print("Hello, " + username.title() + "!")
greet_user('cassio')'''


'''def describe_pet(animal_type, pet_name):
    ###Exibe informações sobre um animal de estimação.
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')'''


'''def describe_pet(pet_name, animal_type='dog'):
    ###Exibe informações sobre um animal de estimação.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('bailey')'''


'''def get_formatted_name(first_name, last_name):
    ###Devolve um nome completo formatado de modo elegante.
    full_name = first_name + ' ' + last_name
    return full_name.title()

dev = get_formatted_name('cássio','camargos')
print(dev)'''


'''def get_formatted_name(first_name, last_name, middle_name=''):
    ###Devolve um nome completo formatado de modo elegante.
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

dev = get_formatted_name('jimi', 'hendrix')
print(dev)

dev = get_formatted_name('john', 'hooker', 'lee')
print(dev)'''


x = 3 + 5j
print(type(x))