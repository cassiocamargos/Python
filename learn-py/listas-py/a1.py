# 1- Elabore um programa que leia dois números e imprima o resultado da soma, da subtração, da multiplicação e da divisão destes números.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

print(f'{n1} + {n2} = {soma}')
print(f'{n1} - {n2} = {sub}')
print(f'{n1} * {n2} = {mult}')
print(f'{n1} / {n2} = {div:.0f}')