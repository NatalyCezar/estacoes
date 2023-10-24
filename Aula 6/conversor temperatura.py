# Conversor de Unidades: Graus Celsius e Fahrenheit

from funcao import graus
from funcao import fah

while True:

    print('\n\t\t -- CONVERSÃO GRAUS CELSIUS/FAHRENHEIT')

    print('1. Transformar Graus Celsius em Fahrenheit')
    print('2. Transformar Fahrenheit em Graus Celsius')
    print('3. Sair')

    op = int(input('Opção: '))
    print('\n')

    if op == 1:
        valor = float(input('Digite a temperatura em Graus Celsius: '))
        print('Temperatura em Fahrenheit: ', graus(valor))

    elif op == 2:
        valor = float(input('Digite a temperatura em fahrenheit: '))
        print('Temperatura em Graus Celsius: ', fah(valor))

    elif op == 3:
        print('Obrigada !')
        break

    else:
        print('Não encontrado')

