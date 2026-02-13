#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('Digite um número inteiro: '))
print('O número digitado foi {}, o seu antecessor é {} e o seu sucessor é {}'.format(num, num-1, num+1))
