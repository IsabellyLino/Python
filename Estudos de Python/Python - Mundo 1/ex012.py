#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 0.05
preco_final = preco - desconto
print('O preço do produto com 5% de desconto é: R${:.2f}'.format(preco_final))
