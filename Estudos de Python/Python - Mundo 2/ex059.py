'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''Escolha a operação desejada:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Digite a opção desejada: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opção == 2:
        multiplicação = n1 * n2
        print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, multiplicação))
    elif opção == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que {}'.format(n2, n1))
        else:
            print('Os números são iguais.')
    elif opção == 4:
        print('Informe os novos números:')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando o programa...')
        sleep(2)
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')