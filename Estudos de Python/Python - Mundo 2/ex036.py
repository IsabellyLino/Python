#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Em quantos anos ele vai pagar? "))
prestacao = valor_casa / (anos * 12)
if prestacao > (salario * 0.3):
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")
    print('Valor da prestação mensal: R${:.2f}'.format(prestacao))
