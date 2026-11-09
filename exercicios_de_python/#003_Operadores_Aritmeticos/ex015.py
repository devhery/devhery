'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidadede dias pelos quais ele foi alugado.  Calcula o preço a pagar, sabendo
que o  carro custa $60 por dia e $0.15 por km rodados.'''

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco = dias * 60 + km * 0.15
print('O total a pagar é de ${:.2f}'.format(preco))
