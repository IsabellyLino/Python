'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
from time import sleep
computador = randint(0, 10)
cont = 0
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
acertou = False
while not acertou:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(2)
    cont +=1
    if jogador == computador:
        acertou = True
        print('Parabéns! Você acertou o número na {}ª tentativa.'.format(cont))
    else:
        print('Você errou! Tente novamente.')
