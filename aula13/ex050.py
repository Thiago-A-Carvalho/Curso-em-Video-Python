"""
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
"""
# Minha resolução
soma = 0
for c in range(1, 500):
    if (c % 2 != 0) and (c % 3 == 0):
        soma += c
print(f'A soma de todos os números impares, de 1 a 500, divisíveis por 3 é {soma}.')
"""
# Resolução do professor
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma dos {cont} valores solicitados é {soma}.')
