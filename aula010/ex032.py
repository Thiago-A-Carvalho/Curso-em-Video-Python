"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
"""
num = int(input('Digite um número inteiro: '))
teste = num % 2
print(teste)
if teste == 0:
    print(f'{num} é um número PAR.')
else:
    print(f'{num} é um número IMPAR.')
