#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
print('Vamos jogar Jokenpô!')
opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)
jogador = input('Escolha Pedra, Papel ou Tesoura: ').capitalize()
print(f'Computador escolheu: {computador}')
if jogador == computador:
    print('Empate!')
elif (jogador == 'Pedra' and computador == 'Tesoura') or \
     (jogador == 'Papel' and computador == 'Pedra') or \
     (jogador == 'Tesoura' and computador == 'Papel'):
    print('Você venceu!')
else:
    print('Computador venceu!')
    