# 5- O cardápio de uma lanchonete é dado pela tabela de preços abaixo. Escreva um programa que leia a quantidade de cada item comprado por um determinado cliente e imprima o valor total da sua compra.
#    Hambúrguer R$ 8,00
#    Batata frita R$ 12,00
#    Refrigerante R$ 3,00
#    Cerveja R$ 5,00
#    Doce R$ 3,00

h = int(input('Quantidade de hamburgueres pedidos: ')) * 8
b = int(input('Quantidade de batatas fritas pedidas: ')) * 12
r = int(input('Quantidade de refrigerantes pedidos: ')) * 3
c = int(input('Quantidade de cervejas pedidas: ')) * 5
d = int(input('Quantidade de doces pedidos: ')) * 3

total = h + b + r + c + d

print(f'\nTotal da conta: R$ {total:.2f}')