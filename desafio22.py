#Crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas;
# b) O nome com todas as letras minúsculas;
# c) Quantas letras ao todo (sem considerar espaços);
# d) Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Em letras maiúsculas: {}'.format(nome.upper()))
print('Em letras minúsculas: {}'.format(nome.lower()))
print('Total de letras é: {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))