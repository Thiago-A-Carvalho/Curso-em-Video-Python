"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

"""
# Minha Resolução

num = int(input('Digite um número para ver sua tabuada: '))
mult = 0
for cont in range(1, 11):
    mult = num * cont
    print(f'{num} X {cont} = {mult}')
    mult += 1
"""
# Resolução do professor
num = int(input('Digite um número para ver sua tabuada: '))
for cont in range(1, 11):
    print(f'{num} X {cont} = {num * cont}')
