'''def boas_vindas_marcos():
    print('ola marcos')
    print('Temos 5 laptop em estoque')

def boas_vindas_ronaldo():
    print('ola ronaldo')
    print('Temos 4 laptop em estoque')

def boas_vindas_ana():
    print('ola ana')
    print('Temos 2 laptop em estoque')

boas_vindas_marcos()
boas_vindas_ronaldo()
boas_vindas_ana()'''


'''def boas_vindas(nome, qtd):
    print(f'Olá {nome}!')
    print(f'Temos {str(qtd)} laptops em estoque.\n')
boas_vindas('Joao', 5)
boas_vindas('Pedro', 4)
boas_vindas('Ana', 2)'''


'''def cliente1(nome):
    print(f'Olá {nome}')
cliente1('Maria')

def cliente2(nome):
    return f'Olá {nome}'
print(cliente2('José'))'''


'''def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2, 3, 4, 7)
print(x)'''


def agencia(**carro):
    return carro

print(agencia(marca = 'audi', modelo = 'a4', cor = 'branco', motor = 2.0))
print(agencia(marca = 'audi', modelo = 'a4', cor = 'branco'))
print(agencia(marca = 'audi', modelo = 'a4'))
