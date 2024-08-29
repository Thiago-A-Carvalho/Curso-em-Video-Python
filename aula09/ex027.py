"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
"""
"""
# Minha Resolução:

nome = str(input('Digite seu nome completo: ')).strip().upper()
contar = nome.count('SILVA')
print(f'Seu nome tem Silva? {contar >= 1}')
"""
# Resolução do professor:
nome = str(input('Qual é o seu nome: ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')
