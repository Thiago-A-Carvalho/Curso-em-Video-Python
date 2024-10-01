"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 25 anos: SÊNIOR
Acima: MASTER 
"""
from datetime import date
# pega o ano atual
anoatual = date.today().year
anonasc = int(input('Digite seu ano de nascimento: '))
idade = anoatual - anonasc
if idade <= 9:
    print(f'''O atleta tem {idade} anos.
Classificação: Mirim.''')
elif idade <= 14:
    print(f'''O atleta tem {idade} anos.
Classificação: Infantil.''')
elif idade <= 19:
    print(f'''O atleta tem {idade} anos.
          Classificação: Junior.''')
elif idade <= 25:
    print(f'''O atleta tem {idade} anos.
Classificação: Sênior.''')
else:
    print(f'''O atleta tem {idade} anos.
Classificação: Master.''')
