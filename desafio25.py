# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Qual seu nome completo? ')).strip()
print('No seu nome tem Silva? {}'.format('SILVA' in nome.upper()))