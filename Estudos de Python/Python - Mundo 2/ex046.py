'''Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
import time
print('Contagem regressiva para os fogos de artifício!')
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print('Feliz Ano Novo! 🎆')