"""frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
'''frutas2 = []

for item in frutas1:
    if 'b' in item:
        frutas2.append(item)'''

frutas2 = [item for item in frutas1 if 'b' in item]

print(frutas2)"""



'''valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)'''

'''valores = [x * 10 for x in range(6)]
print(valores)'''
