"""
Faça um algorítmo que peça ao usuário para digitar uma palavra e verifica se ela é palíndromo
"""

p = input('Digite uma palavra: ')
i = 0
erro = False
psemesp = ''

while i < len(p):  # Tratamento para frases
    if p[i] != ' ':
        psemesp += p[i]
    i += 1

i = 0
while i < len(p)/2:
    if psemesp[i].upper() != psemesp[-(i+1)].upper():
        erro = True
    i += 1

if erro:
    print(f'A palavra {p} não é palíndromo')
else:
    print(f'A palavra {p} é palíndromo')
