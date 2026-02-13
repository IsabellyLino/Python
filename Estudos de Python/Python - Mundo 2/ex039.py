#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(18 - idade))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))