'''
# verificar primeiro digito depois do -    # verificar segundo digito depois do -
    x * 10                                 #   x * 11
    x * 9                                  #   x * 10
    x * 8                                  #   x * 9
    x * 7                                  #   x * 8
    x * 6                                  #   x * 7
    x * 5                                  #   x * 6
    x * 4                                  #   x * 5
    x * 3                                  #   x * 4
    x * 2                                  #   x * 3
                                           #   x * 2
      primeiro digito: 11 - (x % 11)      ###    segundo digito: 11 - (x % 11)  
'''

while True:

    cpf = input('Digite um CPF: ')
    verificado = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -=9
        
        total += int(verificado[index]) * reverso
        
        reverso -=1
        if reverso < 2:
            reverso = 11
            dig = 11 - (total % 11)
            if dig > 9:
                dig = 0
            total = 0

            verificado += str(dig)
        
    if cpf == verificado:
        print('CPF válido')
    else:
        print('CPF inválido')