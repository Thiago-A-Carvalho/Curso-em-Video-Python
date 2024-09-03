"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem. cobrando R$ 0,50 por Km para viagens até 200 Km e R$ 0,45 para viagens mais longas.
"""
"""
Minha resolução:

distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    print(f'O preço da sua passagem é R$ {(distancia * 0.50):.2f} reais.')
else:
    print(f'O preço da sua passagem é R$ {(distancia * 0.45):.2f}')
"""
# Resolução do professor:
distancia = float(input('Qual é a distância da sua viagem? '))
print(f'VocÊ está prestes a inicia uma viagem de {distancia:.2f} Km.')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preç oda sua passagem será de R$ {preço:.2f} reais.')
