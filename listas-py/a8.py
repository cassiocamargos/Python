# 8- O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de  ábrica). Supondo que a porcentagem do distribuidor seja de 12% e os impostos de 45%, elabore um programa que leia o valor de fábrica e imprima o preço final de um carro.

f = float(input('Digite o custo de fabrica do carro: '))

d = f * 0.12
i = f * 0.45
v = f + d + i

print(f'Valor final do carro: R$ {v:.2f}')