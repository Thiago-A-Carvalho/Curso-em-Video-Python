"""
Crie um programa que leia duas notas de um alunos e calcule sua média, mostrando uma mensagem no final, de acordo com a média antingida:
- Média abaixo de 5,0: REPROVADO
- Média entre 5,0 e 6,9: RECUPERAÇÃO
- Média 7,0 ou superior: Aprovado
"""
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {média:.1f}')
if média >= 7.0:
    print(f'Aprovado.')
elif 6.9 >= média >= 5.0:
    print('Recuperação.')
else:
    print(f'Reprovado.')
