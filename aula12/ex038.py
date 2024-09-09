"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. Pergunte o valor da casa, o salário do comprador e quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
valor = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o seu salário? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor / (anos * 12)
print(f'Para pagar uma casa de R$ {valor:.2f} reais em {anos} anos, a prestação é de R$ {prestação:.2f} reais.')
if prestação > salário * 0.3:
    print(f'Empréstimo negado.')
else:
    print(f'Parabéns! Empréstimo aprovado.')
