# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo. 
c1 = float(input('Qual o comprimento da primeira reta? '))
c2 = float(input('Qual o comprimento da segunda reta? '))
c3 = float(input('Qual o comprimento da terceira reta? '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')
