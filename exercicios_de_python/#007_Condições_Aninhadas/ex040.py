nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Sua média foi {}, \033[1;31mREPROVADO!\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {}, \033[1;33mRECURSO!\033[m'.format(media))
elif media > 7:
    print('\033[1;32mAPROVADO!\033[m')
