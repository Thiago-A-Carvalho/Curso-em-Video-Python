"""
Condições Aninhadas
"""
nome = str(input('Qual é o seu nome? '))
if nome == 'Sarah':
    print(f'Que nome lindo!!')
elif nome == 'Bob' or nome == 'Tamira':
    print(f'Seu nome não é muito comum no Brasil.')
elif nome in 'Raimunda, Renata, Regina.':
    print(f'Seu nome começa com R.')
else:
    print('Olá.')
print(f'Tenha um bom dia, {nome}.')
