'''Escreve um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunta o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o
empréstimo será negado.'''

casa = float(input('Valor da casa: $'))
salario = float(input('Salário do comprador: $'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de ${:.2f} em {} anos'.format(casa, anos), end='')
print(' a pretação será de ${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('\033[32mESPRÉSTIMO CONCEDIDO!\033[m')
else:
    print('\033[31mESPRÉSTIMO NEGADO!\033[m')
    