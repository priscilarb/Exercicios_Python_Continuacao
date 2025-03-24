# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

salario = float(input('Qual é o valor do salário? '))
if salario > 1250:
    salario_novo = (salario * 0.10) + salario
else:
    salario_novo = (salario * 0.15) + salario
    
print(f'O novo salário será R$ {salario_novo}')
