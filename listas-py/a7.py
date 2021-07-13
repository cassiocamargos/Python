# 7- Em uma determinada loja, o preço dos produtos na prateleira é mostrado sem se adicionar o imposto. Considerando que o valor do imposto seja de 17% sobre o valor de prateleira, crie um programa que leia o preço de um produto e mostre o valor do imposto e o valor total a ser pago pelo consumidor.

p = float(input('Digite o valor do produto: '))

i = p * 0.17
v = p + i

print(f'Valor de imposto sob produto: R$ {i:.2f}')
print(f'Valor final do produto: R$ {v:.2f}')