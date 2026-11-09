nome = str(input('Qual é seu nome? '))
if nome == 'Herivany':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'António' or nome == 'João':
    print('Seu nome é bem popular em Angola.')
elif nome in 'Jéssica' 'Bela' 'Joana':
    print('Belo nome femenino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))