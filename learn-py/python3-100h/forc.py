palavra = input('Digite uma palavra para ser advinhada: ')
digitadas =[]
chances = int(len(palavra)/2)

print('\n'*50)
while True:
    if chances <= 0:
        print(f'Voce perdeu! A palavra era {palavra}')
        break

    letra =  input('Digite uma letra: ')

    if len(letra) > 1:
        print ('Favor, digitar somente uma letra!')
        continue

    digitadas.append(letra)
    print()

    if letra in palavra:
        print(f'A letra {letra} existe na palavra')
    else:
        print(f'A letra {letra} não existe na palavra')
        digitadas.pop()
    print()

    formacao = ''
    for letra_nova in  palavra:
        if letra_nova in digitadas:
            formacao += letra_nova
        else:
            formacao += '*'
    
    if formacao == palavra:
        print(f'Você ganhou!!! A palavra é {palavra}.')
        break
    else:
        print(formacao)

    if letra not in palavra:
        chances -= 1
    
    if chances > 0:
        print(f'\nVocê ainda tem {chances} chances.')

    print()