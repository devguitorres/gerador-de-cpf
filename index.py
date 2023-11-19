import random
import sys
nove_digitos = ''
cpf_tratado = ''
contador_regressivo1 = 10
contador_regressivo2 = 11
soma1 = 0
soma2 = 0

while True:


    condicao = input('Deseja gerar um novo CPF? [s]im ou [n]ão: ').lower()
    if condicao == 's':
        for _ in range(9):
            nove_digitos += str(random.randint(0,9))
        print(f'Os nove dígitos do seu cpf são {nove_digitos}')
        
        for digito in nove_digitos:
            soma1+= (int(digito)*contador_regressivo1)*10
            contador_regressivo1 -= 1

        
        digito1= soma1%11
        digito1 = digito1 if digito1 <= 9 else 0
        print(f'O seu primeiro dígito é {digito1}')

        dez_digitos = nove_digitos+str(digito1)
        for digito2 in dez_digitos:
            soma2 += (int(digito2)*contador_regressivo2)
            contador_regressivo2 -= 1
        
        digito2 = (soma2*10)%11
        digito2 = digito2 if digito2 <= 9 else 0
        print(f'O segundo dígito é {digito2}')
        cpf_final = f'{nove_digitos}{digito1}{digito2}'
        print(f'O seu novo CPF é {cpf_final}')
        exit()

    elif condicao == 'n':
        print('Ok. Saindo do sistema')
        exit()
    else:
        print('Por favor, digite uma das opções válidas')
