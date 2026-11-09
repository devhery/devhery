from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: # PEDRA
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif computador == 1: # PAPEL
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif computador == 2: # TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')