'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
contador = 10
while contador != 0:
    while primeiro_termo <= decimo_termo:
        print(primeiro_termo, end=' → ')
        primeiro_termo += razao
    print('PAUSA')
    contador = int(input('Quantos termos você quer mostrar a mais? '))
    decimo_termo += contador * razao
print('ACABOU')