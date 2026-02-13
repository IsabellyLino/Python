#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Digite um valor em metros: '))
print('O valor digitado foi {} metros, que equivale a {} centímetros e {} milímetros'.format(valor, valor*100, valor*1000))