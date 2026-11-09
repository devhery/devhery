from  random import randint 
from time import sleep
computador = randint(0, 5)
print('\033[33m-=\033[m' * 28)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=\033[m' * 28)
jogador = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me VENCER!\033[m')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!\033[m'.format(computador, jogador))

