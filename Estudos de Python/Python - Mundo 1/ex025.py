#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite o nome de uma pessoa: ')).strip()
print('SILVA' in nome.upper())