"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
"""
# Minha reoslução: 
from datetime import date
anoatual = date.today().year
ano = int(input('Que ano deseja analisar? Caso seja o ano atual, digite 0: '))
if ano == 0:
    ano = anoatual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
"""
# Reoslução do professor: 
from datetime import date
ano = int(input('Que ano deseja analisar? Caso seja o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year # pega somente o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # condição para ser bissexto
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
