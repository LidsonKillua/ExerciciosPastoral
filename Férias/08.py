"""
Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela pode ou não votar esse ano.
"""

idadevot = 16
anoatual = int(input('Digite o ano atual: '))
anonasc = int(input('Digite o ano que você nasceu: '))

idade = anoatual - anonasc

if idade >= idadevot:
    resultado = 'poderá'
else:
    resultado = 'não poderá'

print(f'Você tem {idade} anos, logo {resultado} votar esse ano.')
