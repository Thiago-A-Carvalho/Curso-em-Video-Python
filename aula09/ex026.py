"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
"""
# Minha Resolução

cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
separa = cidade.split()
teste = separa[0] == "SANTO"
print(teste)
"""
# Minha Resolução do professor:
cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
print(cidade[:5] == 'SANTO')
