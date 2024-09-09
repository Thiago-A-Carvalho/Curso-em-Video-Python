"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
"""
# Minha resolução:

from statistics import median
reta1 = float(input('Comprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))
lista = [reta1, reta2, reta3]
menor = min(lista) # Retorna o menor valor de um conjunto de dados
menor2 = median(lista) # Retorna a mediana de um conjunto de dados. Nesse caso, o segundo menor valor.
maior = max(lista) # Retorna o maior valor de um conjunto de dados
if (menor + menor2) > maior:
    print(f'As retas {lista[0]:.2f}, {lista[1]:.2f} e {lista[2]:.2f} formam um triângulo.')
else:
   print(f'As retas {lista[0]:.2f}, {lista[1]:.2f} e {lista[2]:.2f} não formam um triângulo.') 
"""
# Resolução do professor:
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo.')
