# 6- Uma concessionária de veículos paga a seus funcionários um salário de R$350,00 mais uma comissão de R$200,00 por cada carro vendido. Elabore um programa que leia o número de carros vendidos por um determinado funcionário e imprima seu salário total.

v = int(input('Digite a quantidade de carros vendidos: '))

s = 350 + 200 * v

print(f'Salario total: R$ {s:.2f}')