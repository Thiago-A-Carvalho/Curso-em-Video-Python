"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a ultima vez.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count('A')} vezes.')
print(f'A primeira letra "A" aparece na posição {frase.find('A') + 1}.')
print(f'A ultima vez que a letra "A" aparece é na posição {frase.rfind('A') + 1}.')
