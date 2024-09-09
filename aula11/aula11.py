"""
Cores com Padrão ANSI
escape sequence
\033[m
Cores:
style: 0 (sem estilo), 1 (negrito), 4 (sublinhado) e 7 (inverter fundo e cor de letra)
text: 30 (cinza), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (roxo), 35 (magenta), 36 (ciano) e 37 (branco)
Back: 40 (cinza), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (roxo), 45 (magenta), 46 (ciano)e 47 (branco)
"""
print('\033[30mTeste Cinza\033[m')
print('\033[31mTeste Vermelho\033[m')
print('\033[32mTeste Verde\033[m')
print('\033[33mTeste Amarelo\033[m')
print('\033[34mTeste Roxo \033[m')
print('\033[35mTeste Magenta\033[m')
print('\033[36mTeste Ciano\033[m')
print('\033[37mTeste Branco\033[m')
print('=' * 30)
a = 24
b = 3
print(f'Os valores são \033[1;33;47m{a}\033[m e \033[1;35;43m{b}\033[m!!.')
print('\033[31m=\033[m' * 30)
nome = 'Teste'
cores = {'Vermelho':'\033[31m', 
         'Amarelo':'\033[33m', 
         'Branco':'\033[37m'}

print(f'Prazer em te conhecer {cores['Amarelo']}{nome}{cores['Branco']}!!')
