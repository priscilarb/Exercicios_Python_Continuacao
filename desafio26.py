# Faça um programa que leia uma frase pelo teclado e mostre:
# a) Quantas vezes aparece a letra "A";
# b) Em que posição ela aparece a primeira vez?
# c) Em que posição ela aparece a última vez?
#  
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas vezes aparece a letra A: {}'.format(frase.count('A')))
print('Em que posição ela aparece na primeira vez? {}'.format(frase.find('A') +1))
print('Em que posição ela aparece a última vez? {}'.format(frase.rfind('A') +1))