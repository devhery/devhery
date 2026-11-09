from datetime import date
atual = date.today().year

sexo = str(input('Digite seu sexo [M, m, F ou f]: ')).strip().upper()
if sexo == 'F':
    print('\033[31mSexo negado!\033[m Alistamento obrigatório para sexo masculino.')

elif sexo == 'M':
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar \033[31mIMEDIATAMENTE!\033[m')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18: 
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('\033[31mOpção inválida!\033[m Tente novamente')
