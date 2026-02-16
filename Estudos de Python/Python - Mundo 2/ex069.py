'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
total_maiores = total_homens = total_mulheres_menores = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    if idade > 18:
        total_maiores += 1
    if sexo == 'M':
        total_homens += 1
    elif sexo == 'F' and idade < 20:
        total_mulheres_menores += 1
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total_maiores}')
print(f'Total de homens cadastrados: {total_homens}')
print(f'Total de mulheres com menos de 20 anos: {total_mulheres_menores}')
