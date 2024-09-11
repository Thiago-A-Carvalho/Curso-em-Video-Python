"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
anonasc = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year # pega o ano atual
idade = anoatual - anonasc
menor = 18 - idade # informa quantos anos faltam para chegar em 18 anos
maior = idade - 18 # informa quantos anos tem a mais que 18 anos
print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.')
if idade == 18:
    print(f'Você deve se alistar imediatamente.')
elif idade < 18:
    print(f'''Ainda faltam {menor} anos para o seu alistamento.
Seu alistamento será em {anoatual + menor}''')
else:
    print(f'''Você já deveria ter se alistado há {maior} anos.
Seu alistamento foi em {anoatual - maior}.''')
