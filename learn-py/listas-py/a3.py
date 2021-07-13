# 3- Para realizar a conversão de temperatura da escala Celsius para a escala Fahrenheit é necessário usar a fórmula F = 1.8 * C + 32. Escreva um programa que leia uma temperatura em Celsius e imprima a temperatura convertida para Fahrenheit.

c = float(input("Digite a temperatura em graus celcius: "))

f = 1.8 * c + 32

print (f'{c:.1f} é igual a {f:.1f} graus fahrenheit')