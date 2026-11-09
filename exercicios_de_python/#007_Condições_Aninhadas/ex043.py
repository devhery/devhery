'''Desenvolva uma lógica queleia o peso e a altura de um
cidadão, calcule o seu IMC (Índice De Massa Corporal) e mostre o seu estado nutricional
segundo o seguinte:

-Abaixo de 18.5: Abaixo do peso 
-Entre 18.5 e 25: Peso normal
-De 25 até 30: Excesso de peso
-De 30 até 40: Obesidade
-Acima de 40: Obesidade mórbida'''

peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: (m) '))
imc = peso / (altura ** 2)
print('O IMC do cidadão é de {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO NORMAL')
elif 18.5 <= imc < 25: 
    print('PESO NORMAL, PARABÉNS!')
elif 25 <= imc < 30:
    print('EXCESSO DE PESO'.upper())
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIADA, Cuidado!')