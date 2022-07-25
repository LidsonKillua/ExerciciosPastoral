"""
Faça um algorítmo que peça ao usuário para digitar um caracter C qualquer e uma palavra P qualquer. Contar quantas vezes
C aparece em P. (com while)
"""

c = input('Digite um caracter: ')
p = input('Digite uma palavra: ')
count = i = 0

while i < len(p):
    if p[i].upper() == c.upper():
        count += 1
    i += 1

print(f'O caracter {c} aparece {count} vezes na palavra {p}')

#ou

c = input('Digite um caracter: ')
p = input('Digite uma palavra: ')
print(f'O caracter {c} aparece {p.upper().count(c.upper())} vezes na palavra {p}')
