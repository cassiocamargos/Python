'''bicycles = ['trek', 'cannondale', 'redline', 'specialized'] #lista
print(bicycles)
print(bicycles[0].title()) #a partir do primeiro elemento da lista
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title()+"\n")
print(bicycles[-1].title()) #a partir do ultimo elemento da lista
print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title()+"\n")
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
print("\n\n")'''


'''motorcycles = ['honda', 'yamaha', 'suzuki']
print(str(motorcycles)) #str transforma numa string
motorcycles[0] = 'ducati' #modifica elemento da lista
print(str(motorcycles)+"\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(str(motorcycles))
motorcycles.append('ducati') #acrescenta elemento ao final da lista
print(str(motorcycles)+"\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(str(motorcycles))
motorcycles.insert(0,'ducati') #insere elemento na posição desejada
print(str(motorcycles)+"\n")


del motorcycles[-1] #deleta elemento da posição desejada
print(str(motorcycles)+"\n")

popped_motorcycle = motorcycles.pop() #remove o último (por padrão) item de uma lista, mas permite que você trabalhe com esse item depois da remoção
print(motorcycles)
print(str(popped_motorcycle).title()+"\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(str(motorcycles))
motorcycles.remove('ducati') #remove elemento da lista pelo valor
print(str(motorcycles)+"\n")'''

'''cars = ['bmw', 'audi', 'toyota', 'subaru']
print(str(cars))
cars.sort() #ordena permanentemente a lista em ordem alfabetica
print(str(cars)+"\n")
cars.sort(reverse=True) #ordena permanentemente a lista em ordem alfabetica inversa
print(str(cars)+"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(str(cars))
print(str(sorted(cars))) #ordena temporariamente a lista em ordem alfabetica
print(str(cars))
cars.reverse() #imprime a lista de forma inversa
print(str(cars))
print(len(cars)+"\n") #tamanho da lista'''

'''######TRABALHANDO COM LISTAS######
cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars: #laço for - A saída é uma exibição simples de cada nome da lista
    print ("\t"+str(car).title()+", that was a great motorcycle race!")
print("\n\tThank you, everyone!")
print("\n\n")'''

'''#FATIANDO UMA LISTA
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])'''

'''#Percorrendo uma fatia com um laço
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())'''

'''#Copiando uma lista
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)'''

'''#Transferindo itens de uma lista para outra
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
confirmed_users.sort()
for confirmed_user in confirmed_users:
    print(confirmed_user.title())'''

#Removendo todas as instâncias de valores específicos de uma lista
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)