'''Desenvolva um programa qie pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando $0.50 por km para
viagens de até 200km e $0.45 por viagens mais longas'''

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você esta preste a começar uma viagem de {}km.'.format(distancia))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de \033[0;44m${:.2f}\033[m'.format(preco))