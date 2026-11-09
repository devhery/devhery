print('=' * 30, '\033[1;33mLOJA\033[m \033[1;31mANGOLANA\033[m', '=' * 30)
preco = float(input('Preço das compras: kz '))

print('''Formas de Pagamento
[1] À vista (Dinheiro / Transfência)
[2] À vista no cartão Multicaixa
[3] Até 2x no cartão / Prestação
[4] 3x ou mais no cartão''')
opcoa = int(input('Qual é a opção? '))

if opcoa == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de {:.2f}kz vai custar {:.2f}kz no final com 10% de desconto.'.format(preco, total))
elif opcoa == 2:
    total = preco
    print('Sua compra de {:.2f}kz será paga no valor normal de {:.2f}kz'.format(preco, total))
elif opcoa == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}kz SEM JUROS. Total {:.2f}kz'.format(parcela, total))
elif opcoa == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas prestações? '))
    if totalparc < 3:
        print('\033[31mOpção de parcelamento inválida para 3x ou mais. Por favor escolha 3 ou mais.\033[m')
    else:
        parcela = total / totalparc
        print('Sua compra está parcelada em {}x de {}kz COM JUROS.'.format(totalparc, parcela))
        print('Sua compra de {:.2f}kz vai custar {:.2f}kz'.format(preco, total))
else:
    total = preco
    print('\033[31mOpcao de pagamento inválida. Tente novamente.\033[m')
