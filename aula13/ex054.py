"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input('Digite um número: '))
contdiv = 0
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end= ' ')
        # Conta quantas vezes o número é divisível
        contdiv += 1
    else:
        print('\033[31m', end= ' ')
    print(c, end= ' ')
if contdiv == 2:
    print(f'\n\033[mO número {num} foi divisível {contdiv} vezes. Por isso ele É PRIMO.')
elif contdiv > 2:
    print(f'\n\033[mO número {num} foi divisível {contdiv} vezes. Por isso ele NÃO É PRIMO.')
else:
    print(f'\n\033[mO número {num} foi divisível {contdiv} vez. Por isso ele NÃO É PRIMO.')
    