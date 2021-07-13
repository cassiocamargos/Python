variavel = ['cassio', 'camargos', 'fernandes', 'silva']

for valor in variavel:
    if valor.startswith('c'):
        print(f'{valor} começa com c')
    else:
        print(f'{valor} não começa com c')
print()


for v in variavel:
    if v.lower().startswith('f'):
        print(f'{v} começa com a letra "f"')
        break
else:
    print('Não existe uma palavra que começa com "f"')