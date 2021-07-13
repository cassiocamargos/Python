# 10- Escreva um programa que, lendo o raio de um círculo, imprima sua a área e sua circunferência. Onde: Comprimento = 2 * PI * Raio e Área = PI * Raio2

import math

r = float(input('Digite o valor do raio da circunferencia: '))

d = 2 * r
c = 2 * (math.pi) * r
a = (math.pi) * r**2

print(f'Diametro da circunferencia: {d:.2f}')
print(f'Comprimentoda circunferencia: {c:.2f}')
print(f'Area da circunferencia: {a:.2f}')