"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostra os 10 primeiros termos dessa progressão.
"""
"""
# Minha resolução:

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(termo, termo + (razão * 10), razão):
    print(c, end= ' -> ')
print('Acabou!')
"""
# Resolução do professor:
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, end= '-> ')
print('ACABOU')
