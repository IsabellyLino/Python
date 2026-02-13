'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
print('Digite o comprimento de três retas para saber se elas podem formar um triângulo.')
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 < reta1 + reta2):
    print('As retas podem formar um triângulo!')
    if reta1 == reta2 == reta3:
        print('O triângulo formado é EQUILÁTERO.')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O triângulo formado é ISÓSCELES.')
    else:
        print('O triângulo formado é ESCALENO.')
else:
    print('As retas não podem formar um triângulo!')