#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma = 0
media = 0
maior = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = soma / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher))