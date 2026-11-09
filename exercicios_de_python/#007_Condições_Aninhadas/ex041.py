'''A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria,  de
acordo com a idade:
-> Até 9 anos: MIRIM                    ->Até 19 anos: JUNIOR   
-> Até 14 anos: IMFANTIL                 ->Até 25 anos: SÊNIOR
-> Acima: MASTER'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[1;36mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[1;33mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[1;32mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[1;34mSÊNIOR\033[m')
else:
    print('Classificação: \033[1;31mMASTER\033[m')