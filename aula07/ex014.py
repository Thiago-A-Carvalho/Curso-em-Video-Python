# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.
preço = float(input('Informe o valor do produto: R$ '))
preçod = preço-(preço*0.05)
print(f'O preço do produto é R$ {preço:.2f} reais, com o desconto de 5% sai por, R$ {preçod:.2f} reais.')
