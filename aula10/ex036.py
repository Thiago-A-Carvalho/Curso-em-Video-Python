"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
"""
# Minha resolução:

salario = float(input('Qual o salário do funcionário? R$ '))
if salario > 1250.00:
    print(f'Quem ganhava R${salario:.2f}, com um aumento de 10%, passa a ganhar R$ {(salario * 0.10) + salario:.2f}.')
else:
    print(f'Quem ganhava {salario:.2f}, com um aumento de 15%, passa a ganhar R$ {(salario * 0.15) + salario:.2f}.')
"""
# Resolução do professor:
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {novo:.2f}')
