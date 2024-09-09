"""
Escreva um programa que leia um número inteiro qualquer e peça para o usário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:')
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Opção: '))
