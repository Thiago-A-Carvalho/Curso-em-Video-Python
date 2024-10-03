"""
Desenvolva uma lógica que leia o peso e a aultura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'''Seu IMC é de {imc:.2f}.
Você está abaixo do peso.''')
elif 18.5 <= imc < 25:
    print(f'''Seu IMC é de {imc:.2f}.
Parabéns, você está no peso ideal.''')
elif 25 <= imc < 30:
    print(f'''Seu IMC é de {imc:.2f}.
Você está com sobrepeso.''')
elif 30 <= imc < 40:
    print(f'''Seu IMC é de {imc:.2f}.
Você está com obesidade. Cuidado.''')
else:
    print(f'''Seu IMC é de {imc:.2f}.
Você está com obesidade mórbida. Cuidado!''')
    