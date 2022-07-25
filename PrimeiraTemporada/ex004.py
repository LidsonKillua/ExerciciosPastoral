"""
Construa um algorítmo que peça para o usuário digitar um texto e um número X e imprima o caracter da posição X do texto
"""

texto = input('Digite um texto: ')
num = int(input('Digite um número: '))

if num < len(texto):
    print(f'O caractere da posição {num} no texto é {texto[num]}')
