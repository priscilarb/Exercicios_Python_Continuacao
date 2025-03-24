# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)
print('Vamos adivinhar o número que eu pensei?')
num = int(input('Escolha um número entre 0 e 5: '))
print('Aguarde...')
sleep(3)
if num == computador:
    print('Acertou.. Você ganhou!')
else:
    print('Errou.. Ganhei de você!')