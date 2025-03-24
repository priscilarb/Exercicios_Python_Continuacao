# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dógitos separados:
num=int(input('Digite um número: '))
u = num // 1 % 10
c = num // 10 % 10
d = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(c))
print('Centena: {}'.format(d))
print('Milhar: {}'.format(m))