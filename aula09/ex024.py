"""
Análise:
- len(variável) informa o tamanho em caracteres de um texto 
- variável.count('letra/palavra/frase') conta a quantidade de vezes que o caractere aparece. Possível adicionar fatiamento.
- variável.find('letra,palavra,frase') retorna em que posição o caractere iniciou. -1 significa não encontrado.

Transformação:
- variável.replace('Palavra procurada', 'Palavra que quero utilizar') substitui um elemento por outro.
- variável.upper() transforma tudo em maiúsculo.
- variável.lower() transforma tudo em minúsculo.
- variável.capitalize() transforma o primeiro caractere da string para maiúsculo e o restante para minúsculo.
- variável.title() faz o que o capitalize faz, porém, palavra por palavra.
- variável.strip() remove espaços antes e depois da string.
- variável.rstrip() remove só os espaços a direita da string (no final).
- variável.lstring() remove só os espaços a esquerda da string (no inicio).

Divisão:
- variável.split() divide uma string em uma lista, onde cada elemente é separado por seu caractere de split, que por padrão é o "espaço"
- 'caractere desejado'.join(variável) junta todos os elementos de frase separados por um caractere predefinido
"""
# Testes
frase = 'Curso em Vídeo'
print(frase)
print(frase[9])
print(frase[:9])
print(frase[2:])
print(frase[1:20:3])
print(frase[::2])
print(frase[::-2])
print(len(frase))
print(len('Oi professor'))
print(len(frase[:10]))
print(frase.count('i'))
print(frase.count('e', 0, 9))
print(frase.count('em'))
print(frase.find('e'))
print(frase.find('Vídeo'))
print(frase.find('Video'))
print(frase.replace('Vídeo', 'Python'))
print(frase.upper())
print(frase.lower())
print(frase.lower().find('em'))
print(frase.capitalize())
print(frase.title())
frase = '  Curso em Vídeo Python  '
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
print(frase.split())
frase2 = frase.split()
print(' '.join(frase2))
