"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Sarah':
    print(f'Que nome lindo! Bom dia, {nome}.')
else:
    print(f'Bom dia, {nome}.')
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média é {m:.2f}')
if m >= 6:
    print(f'Sua média é boa. Parabés pelo resultado')
else:
    print('Sua média está abaixo de 6,00. Estude mais.')
