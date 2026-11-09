'''Aprimoração do "ex035.py"'''
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos oslados diferentes

print('\033[33m-=\033[m' * 18)
print('\033[34mAnalisador de triângulos\033[m')
print('\033[33m-=\033[m' * 18)
r1 = float(input('Primeiro segmento: '))
r2  = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32mPODEM FORMAR UM TRIÂNGULO \033[m', end='')
    if r1 == r2 == r3:
        print('\033[32mEQUILÁTERO!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[32mESCALENO!\033[m')
    else:
        print('\033[32mISÓSCELES\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m')