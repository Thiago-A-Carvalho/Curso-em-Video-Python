"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsídere-o.
"""
soma = 0
contador = 0
for cont in range(1, 7):
    num = int(input(f'Digite o {cont}° número: '))
    if num % 2 == 0:
        soma += num
        contador += 1
if contador == 0:
    print('Você não digitou nenhum número par.')
elif contador == 1:
 print(f'Você digitou {contador} número par e ele é {soma}.')
else:
   print(f'Você digitou {contador} números pares e a soma deles é {soma}.')
