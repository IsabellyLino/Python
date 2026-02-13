'''Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal 
– 3x ou mais no cartão: 20% de juros'''
preco = float(input('Digite o preço do produto: R$ '))
print('''Escolha a forma de pagamento:
     [1] - à vista dinheiro/cheque: 
     [2] - à vista no cartão: 
     [3] - em até 2x no cartão:  
     [4] - 3x ou mais no cartão: ''')
opcao = int(input('Opção: '))
if opcao == 1:
    valor_final = preco * 0.90
    print(f'Valor a ser pago: R$ {valor_final:.2f} (10% de desconto)')
elif opcao == 2:
    valor_final = preco * 0.95
    print(f'Valor a ser pago: R$ {valor_final:.2f} (5% de desconto)')
elif opcao == 3:
    valor_final = preco
    print(f'Valor a ser pago: R$ {valor_final:.2f} (sem desconto)')
elif opcao == 4:
    valor_final = preco * 1.20
    print(f'Valor a ser pago: R$ {valor_final:.2f} (20% de juros)')
else:
    print('Opção inválida!')
