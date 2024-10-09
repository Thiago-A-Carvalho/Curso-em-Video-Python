"""
for c in range(1, 6):
    print(c)
print('-' * 10)

for c in range(6, 0, -2):
    print(c)
print('-' * 10)

for c in range(0, 6):
    print('Teste')
print('-' * 10)

n = int(input('Digite um número: '))
for c in range(0, n + 1, 2):
    print(c)
print('Fim!')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
print('Fim!')
"""
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma de todos os valores é {s}')
