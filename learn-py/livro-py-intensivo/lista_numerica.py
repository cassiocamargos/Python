'''
#A função range() de Python facilita gerar uma série de números. - Para um numero antes do especificado (de 1 a 5).
for value in range(1,6): 
    print(value)'''

'''
#Podemos usar list() para converter esse mesmo conjunto de números em uma lista.
numbers = list(range(1,6)) 
print("\n"+str(numbers)+"\n")'''

'''
#Também podemos usar a função range() para dizer a Python que ignore alguns números em um dado intervalo. Nesse exemplo, a função range() começa com o valor 2 e então soma 2 a esse valor. O valor 2 é somado repetidamente até o valor final, que é 11, ser alcançado ou ultrapassado.
even_numbers = list(range(2,11,2)) 
print(str(even_numbers)+"\n\n")'''

'''#Lista dos dez primeiros quadrados perfeitos (isto é, o quadrado de cada inteiro de 1 a 10). Começamos com uma lista vazia chamada squares. Dizemos a Python para percorrer cada valor de 1 a 10 usando a função range(). No laço, o valor atual é elevado ao quadrado e armazenado na variável square. Cada novo valor de square é concatenado à lista squares.
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    squares.append(value**2) #alternativa
print(str(squares)+"\n\n")'''

'''#LIST COMPREHENSION (abrangência de lista) - Uma list comprehension combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente. 
squares = [value**2 for value in range(1,11)]
print(squares)'''


'''#Estatísticas simples comumalista de números.
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(str(digits)+"\n")

print("Menor valor: "+(str(min(digits))))

print("Maior valor: "+(str(max(digits))))

print("Soma dos valores: "+(str(sum(digits))))'''

'''#for value in range(1,21):
value = list(range(1,21))
print(value)'''

'''#value =  list(range(1,1001))
for value in range(1,1001):
    print(value)'''

'''value=list(range(1,1001))
print("Menor valor: "+(str(min(value))))
print("Maior valor: "+(str(max(value))))
print("Soma dos valores: "+(str(sum(value))))'''

'''value = list(range(1,20,2))
print(value)'''
    