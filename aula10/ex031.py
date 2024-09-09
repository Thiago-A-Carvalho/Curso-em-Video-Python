"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassa 80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custa R$ 7,00 por cada km acima do limite.
"""
velocidade = float(input('Informe a velocidade atual do seu carro: '))
limite = 80.00
multa = (velocidade - limite) * 7
if velocidade > limite:
    print(f'Você foi multado em R$ {multa:.2f} reais, por excesso de velocidade.')
else:
    print(f'Você está trafegando dentro do limite de velocidade.')
