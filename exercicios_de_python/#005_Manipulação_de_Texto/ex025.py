# in -> operador
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva {}'.format('silva' in nome.lower()))
