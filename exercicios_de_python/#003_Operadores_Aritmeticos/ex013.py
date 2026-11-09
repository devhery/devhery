salario = float(input('Qual é o salário do Funcionario? $'))
aumento = salario + (salario * 15 / 100)
print('Um fucionário que ganhava ${}, com 15% de aumento, passa a receber ${:.2f}'.format(salario, aumento))
