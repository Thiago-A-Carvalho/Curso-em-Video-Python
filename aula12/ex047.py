"""
Crie um programa que faça o compuador jogar Jokenpô com você.
"""
from random import randint
from time import sleep
opções = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2) # Sorteia um número aleatório dentro do intervalo escolhido
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1) # Da um tempo até a próxima ação
print('KEN')
sleep(1)
print('PÔ')
print(f'''{"=" * 20} 
Computador jogou {opções[computador]}
Você jogou {opções[jogada]}
{"=" * 20}''')
if computador == 0: # Computador escolheu PEDRA
    if jogada == 0: # Você escolheu PEDRA
        print('EMPATE!')
    elif jogada == 1: # Você escolheu PAPEL
        print('Parabéns, você VENCEU!')
    elif jogada == 2: # Você escolheu TESOURA
        print('Computador VENCEU. Tente de novo.')
    else:
        print(f'Opção inválida. Tente novamente.')
elif computador == 1: # Computador escolheu PAPEL
    if jogada == 0: # Você escolheu PEDRA
        print('Computador VENCEU. Tente de novo!')
    elif jogada == 1: # Você escolheu PAPEL
        print('EMPATE!')
    elif jogada == 2: # Você escolheu TESOURA
        print('Parabéns, você VENCEU!')
    else:
        print(f'Opção inválida. Tente novamente.')
elif computador == 2: # Computador escolheu TESOURA
    if jogada == 0: # Você escolheu PEDRA
        print('Parabéns, você VENCEU!')
    elif jogada == 1: # Você escolheu PAPEL
        print('Computador VENCEU. Tente de novo!')
    elif computador == 2: # Você escolheu TESOURA
        print('EMPATE')
    else:
        print(f'Opção inválida. Tente novamente.')
