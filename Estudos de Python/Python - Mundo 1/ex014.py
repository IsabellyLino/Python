#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(celsius, fahrenheit))