soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    soma += num
    cont += 1
print(f'Você informou o número {cont} e a soma foi {soma}')