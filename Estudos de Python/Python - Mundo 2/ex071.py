'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
valor = int(input('Digite o valor a ser sacado: R$'))
cedulas = [50, 20, 10, 1]
print('O caixa eletrônico vai entregar:')
while valor > 0:
    for cedula in cedulas:
        if valor >= cedula:
            quantidade = valor // cedula
            valor -= quantidade * cedula
            print(f'{quantidade} cédula(s) de R${cedula}')
            
