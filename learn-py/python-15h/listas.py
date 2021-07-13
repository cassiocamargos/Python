'''cidades = ['Rio de Janeiro', 'sao paulo', 'salvador']
cidades[0] = 'brasilia'
cidades.append('santa catarina')
cidades.remove('salvador')
cidades.insert(1, 'salvador')
cidades.pop(1)
cidades.sort()
print(cidades)'''


'''numeros = [2, 3, 4, 5]
letras = ['a', 'b','c', 'd']
final = numeros + letras
print(final)

numeros = [2, 3, 4, 5]
letras = ['a', 'b','c', 'd']
numeros.extend(letras)
print(numeros)'''


'''itens = [['item1','item2'], ['item3','item4']]
print(itens[0])
print(itens[0][0])
print(itens[0][1])
print(itens[1])
print(itens[1][0])
print(itens[1][1])'''


"""produtos = ['arroz', 'feijao', 'laranja','banana']

item1, item2, item3, item4 = produtos

'''item1 = produtos[0]
item2 = produtos[1]
item3 = produtos[2]
item4 = produtos[3]'''

print(item1)
print(item2)
print(item3)
print(item4)"""


'''produtos = ['arroz', 'feijao', 'laranja','banana', 5, 6, 7, 8]

item1, item2, *outros, item8 = produtos

print(item1)
print(item2)
print(outros)
print(item8)'''


'''valores = [50, 80, 110, 150, 170]
for x in valores:
    print(f'o valor final do produto é de R${x}')'''


'''cor_cliente = input('digite a cor desejada: ')

cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores:
    print('cor em estoque')
else:
    print('nao temos essa cor em estoque')'''


'''cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]
x = zip(cores, valores)
print(list(x))'''


'''frutas_usuario = input('digite o nome das frutas separadas por virgula: ')
frutas_lista = frutas_usuario.split(', ')
print(frutas_lista)'''


cores_lista = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tupla = ('amarelo', 'verde', 'azul', 'vermelho')
