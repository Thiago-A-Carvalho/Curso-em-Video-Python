"""
Faça um programa que leia trÊs números e mostre qual deles é o maio e qual deles é o menor.
"""
"""
# Minha resolução:

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
lista = [num1, num2, num3]
print(f'O maior valor é {max(lista)}.') # retorna o maior valor de um intervalo ou lista. Se str comparação alfabética
print(f'O menor valor é {min(lista)}.') # retorna o menor valor de um intervalo ou lista. Se str comparação alfabética
"""
# Resolução do professor:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor é {menor}.')
print(f'O maior valor é {maior}.')