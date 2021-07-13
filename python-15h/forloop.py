



'''for numero in range(1,20,2):
    print(numero)'''

'''for letra in 'Google':
    print(letra)'''

'''palavra = 'Google'
for letra in palavra:
    print(f'{letra} está na palavra {palavra}')'''


'''compra_confirmada = True
dados_compra = 'Compra e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu email')
        break
else:
    print('Falha na compra')'''


'''for n1 in range(1,6):
    print('Produto ' + str(n1))
    for n2 in range(5):
        print(n1,n2)'''


'''palavra = 'FANTASTICO'
for espaco in palavra:
    print(f'{espaco} ', end='')'''


'''linhas = 6
colunas = 6
simbolo = '#'

for l in range (linhas):
    for c in range(colunas):
        print (simbolo, end='')
    print()'''


'''valor= 100
dia = 0
while valor > 20: 
    dia += 1
    print(f'No dia {dia} o valor do produto será vendido por R${valor}')
    valor -= 5'''


valor = int(input('Digite o valor do produto em R$: '))
while valor > 20:
    valor = valor * 1.1
    print(f'O valor final do produto será de R${valor}')
    break