"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu o programa.
"""
"""
# Minha resolução:

from random import randint
print('-' * 50)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar qual...')
print('-' * 50)
aleatorio = randint(0, 5) # Sorteia um número aleatório dentro do intervalo escolhido
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando...')
if num == aleatorio:
    print('Parabéns, você venceu!')
else:
    print(f'Você perdeu. Eu pensei no número {aleatorio} e não no {num}.')
"""
# Resolução do professor:
from random import randint
from time import sleep
print('-' * 30)
print('Estou pensando em um número entre 0 e 5. Tente adivinhar qual...')
print('-' * 30)
computador = randint(0, 5) # Sorteia um número aleatório dentro do intervalo escolhido
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'Eu pensei no número {computador} e não no {jogador}.')
