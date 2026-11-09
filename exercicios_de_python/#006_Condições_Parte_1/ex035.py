print('\033[33m-=\033[m' * 18)
print('\033[34mAnalisador de triângulos\033[m')
print('\033[33m-=\033[m' * 18)
r1 = float(input('Primeiro segmento: '))
r2  = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[32mPODEM FORMAR UM TRIÂNGULO!\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m')