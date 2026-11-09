'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, motrar uma mensagem
dizendo que ele foi multado.
A multa vai custar $10.00 por cada km acima do limite.'''

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m')
    multa = (velocidade-80) * 10
    print('\033[31mVocê deve pagar uma multa de\033[m \033[33m${:.2f}\033[m'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')

