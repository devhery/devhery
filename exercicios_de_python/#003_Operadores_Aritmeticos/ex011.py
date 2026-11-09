# Faça um programa que leia a largura e altura de uma parede em metros,
# calcule a área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l*h
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l, h, a))
t = a / 2
print('Para pintar essa parede precisará de {}l de tinta'.format(t))