
'''try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('index nao existe')'''


try:
    valor = int(input('digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('favor digitar um valor numerico')
    
# else nao deixa o programa continuar caso haja erro
else:
    print('usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)

# finally continua o codigo apos erro
finally:
    print('codigo ok')
