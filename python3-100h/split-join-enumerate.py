txt = 'O Brasil é o país do futebol, o Brasil é penta.'
print(txt)
print()

lista = txt.split(' ')
print(lista)
print()

txt2 = '_'.join(lista)
print(txt2)
print()

for indice, valor in enumerate(lista):
    print(indice, valor)