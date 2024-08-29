"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
"""
"""
# Minha Resolução:

nome = str(input('Qual o seu nome: ')).strip().title()
print(f'Prazer em te conher!')
separar = nome.split()
print(f'Seu primeiro nome é: {separar[0]}.')
contar = len(separar)
print(f'Seu último nome é: {separar[contar - 1]}.')
"""
# Resolução do professor:
nome = str(input('Qual o seu nome: ')).strip().title()
print(f'Prazer em te conher!')
separar = nome.split()
print(f'Seu primeiro nome é: {separar[0]}.')
print(f'Seu último nome é: {separar[len(separar) - 1]}.')
