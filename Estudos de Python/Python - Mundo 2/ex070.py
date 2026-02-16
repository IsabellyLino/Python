'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total_gasto = 0
total_produtos_mais_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')
while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$'))
    total_gasto += preco
    if preco > 1000:
        total_produtos_mais_1000 += 1
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome
    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {total_produtos_mais_1000}')
print(f'Produto mais barato: {produto_mais_barato} com preço de R${preco_mais_barato:.2f}')
