"""
Escreva um programa que leia um número inteiro qualquer e peça para o usário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Opção: '))
if opção == 1:
    print(f'O núemro {num} convertido para BINÁRIO é igual a {bin(num)[2:]}') # Converte o número para binário
elif opção == 2:
    print(f'O núemro {num} convertido para OCTAL é igual a {oct(num)[2:]}') # Converte o número para octal
elif opção == 3:
    print(f'O núemro {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}') # Converte o número para hexadecimal
else:
    print(f'Opção inválida.')
