# 11- Elabore um programa que seja capaz de ler um valor em reais e transformar este valor em dólares. A taxa de conversão não deve ser fixa, deve ser informada pelo usuário do programa.

r = float(input('Digite o valor em reais: '))
c = float(input('Digite a taxa de conversão para dolares: '))

d = r / c

print(f'Valor em dolares: US$ {d:.2f}')