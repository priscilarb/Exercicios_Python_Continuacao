# Desenvolva um programa que pergunte a distância de uma viagem em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.

distancia = float(input('Quantos quilômetros será sua viagem? '))
if distancia <= 200:
    valor_viagem = distancia * 0.50
else:
    valor_viagem = distancia * 0.45

print(f'Sua viagem custará R$ {valor_viagem:.2f}')
