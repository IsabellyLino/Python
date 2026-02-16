#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um número inteiro: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = 'P' if total % 2 == 0 else 'I'
    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} - {tipo}')
    if escolha == tipo:
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'Game Over! Você venceu {vitorias} vezes consecutivas.')
