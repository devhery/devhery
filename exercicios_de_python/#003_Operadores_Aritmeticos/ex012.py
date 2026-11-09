# Faça um algoritmo que leia o preço de produto
# e mostre o seu novo preço, com 5% de desconto
preco = float(input('preço do produto: $'))
novo = preco - (preco * 5 / 100)
print('Para ${:.2f} com um desconto de 5% será deduzido para: ${:.2f} '.format(preco, novo))
