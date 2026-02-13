#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos Km foram percorridos? '))
preco = (dias * 60) + (km * 0.15)
print('O preço a pagar pelo aluguel do carro é: R${:.2f}'.format(preco))
gasolina = (km /12) * 6.10
print('O valor gasto com gasolina é: R${:.2f}'.format(gasolina))
print('O valor total a pagar é: R${:.2f}'.format(preco + gasolina))