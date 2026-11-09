# Condiçâo simples

'''nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Que nome lindo você tem!')
print('Bom dia, {}'.format(nome))'''

# Condição composta

'''tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--Fim--')'''

# Condição simplificada

'''tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo'if tempo <=3 else 'Carro velho')
print('--Fim--')'''

# Exercício de teste:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Média baixa, ESTUDE MAIS!')