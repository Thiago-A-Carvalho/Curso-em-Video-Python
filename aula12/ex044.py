"""
Refaça o DESAFIO 037 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
"""
# Minha resolução 1:
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2) and (r1 == r2 == r3):
    print(f'Os segmentos acima PODEM FORMAR um triânfulo EQUILÁTERO.')
elif (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2) and ((r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1)):
    print(f'Os segmentos acima PODEM FORMAR um triânfulo ISÓSCELES.')
elif (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2) and (r1 != r2 != r3 != r1):
    print(f'Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo.')
"""
# Minha resolução 2:
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print(f'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print(f'Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
    else:
        print(f'Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
else:
    print(f'Os segmentos acima NÃO PODEM FORMAR um triângulo.')