"""
Crie um programa que leia o nome de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo, sem considerar espaços;
- Quantas letras tem o primeiro nome.
"""
"""
# Minha resolução: 

nome = input('Digite seu nome completo: ')
print(f'Seu nome é: {nome}')
print(f'Em maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
nome2 = nome.replace(' ', '')
print(f'Total de letras sem espaços: {len(nome2)}')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e possui {len(nome[0])} letras')
"""
# Resolução do professor:
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...')
print(f'Em maiúsculo: {nome.upper()}')
print(f'Em minúsculo: {nome.lower()}')
print(f'Total de letras sem espaço: {len(nome) - nome.count(' ')}')
# print(f'Seu primeiro nome tem {nome.find(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e possui {len(separa[0])} letras')
