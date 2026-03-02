'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
produtos = ('Lápis', 1.50,
            'Caneta', 2.00,
            'Caderno', 15.00,
            'Mochila', 120.00)
print('-' * 30)
print("LISTAGEM DE PREÇOS")
print('-' * 30)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<20} R${produtos[i + 1]:>7.2f}')
print('-' * 30)
