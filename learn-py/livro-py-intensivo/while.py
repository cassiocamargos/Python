'''c = 0
while c <= 5:
    print(c)
    c += 1'''

'''c = 0
while True:
    print(c)
    if c==5:
        break
    c += 1'''
    
'''c = 0
while c <= 5:
    if c==0:
        c+=1
        continue
    print(c)
    c += 1'''   

'''contador = 0
acumulador = 0
while contador <= 10:
    print(f'{contador} - {acumulador}')
    contador += 1
    acumulador += contador'''

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_str = ''

while contador < tamanho_frase:
    print(frase[contador])
    '''print(nova_str)
    nova_str += frase[contador]'''
    contador += 1

print(nova_str)


'''#Condição de saída
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)'''

'''#Usando uma flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)'''


'''#Usando break para sair de um laço
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")'''

'''#Usando continue em um laço - a instrução continue diz a Python para ignorar o restante do laço e voltar ao início
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)'''