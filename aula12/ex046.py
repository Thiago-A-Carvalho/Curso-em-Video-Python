"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print(f'{' LOJAS CARVALHO ':=^30}')
compra = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pagamento = int(input('Qual é a forma de pagamento? '))
if pagamento == 1:
    total = compra - (compra * 0.1)
    print(f'Sua compra de R$ {compra:.2f} vai custar R$ {total:.2f} reais.')
elif pagamento == 2:
    total = compra - (compra * 0.05)
    print(f'Sua compra de R$ {compra:.2f} vai custar R$ {total:.2f} reais.')
elif pagamento == 3:
    valorparc = compra / 2
    print(f'Sua compra de R$ {compra:.2f} será parcelada em 2x de R$ {valorparc:.2f} reais, sem juros.')
elif pagamento == 4:
    nparcelas = int(input('Qual será o número de parcelas? '))
    valorparc = (compra + (compra * 0.2)) / nparcelas
    total = compra + (compra * 0.2)
    print(f'''Com o juros, sua compra será parcelada em {nparcelas}x de R$ {valorparc:.2f} reais.
Sua compra de R$ {compra:.2f} vai custar R$ {total:.2f} reais.''')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')
