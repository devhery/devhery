'''Escreva um programa que pergunte o salário de um funcionario e
calcule o valor do seu aumento.
Para salários superiores a $1250, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Qual é o salário do funcionario? $'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava ${} passa a ganhar ${:.2f} agora.'.format(salario, novo))