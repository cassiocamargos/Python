# 9- Em um curso de programação de computadores, a nota final de um estudante é dada a partir de seu desempenho em três aspectos. Existe uma prova teórica que vale 30% da nota final. Uma segunda prova teórica que equivale a 20%. E, uma última prova, que equivale a 50% da nota. Elabore um programa que leia a nota das três avaliações e imprima a nota final do estudante.

n1 = float(input('Digite a nota da primeira prova: ')) * 0.30
n2 = float(input('Digite a nota da segunda prova: ')) * 0.20
n3 = float(input('Digite a nota da terceira prova: ')) * 0.50

nf = n1 + n2 + n3

print(f'Nota final: {nf:.0f}')