#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
din = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = din / 5.25
print(f'Com R${din:.2f} você pode comprar US${dolar:.2f}')
