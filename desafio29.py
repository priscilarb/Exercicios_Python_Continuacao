# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
 
velocidade = float(input('Qual a velocidade que o carro passou no radar? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade permitida que é de 80 km/h.\nPagará uma multa de R$ {multa:.2f}')
else:
    print('Você está dentro do limite permitido!')