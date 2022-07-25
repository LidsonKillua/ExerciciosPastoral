"""
Construa um algorítmo que pede para o usuário digitar um texto e verifique se o texto termina com vogal
"""

texto = input('Digite um texto: ')

if texto[-1].upper() in 'AEIOU':
    print('O texto termina com vogal.')
else:
    print('O texto não termina com vogal.')
