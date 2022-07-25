"""
Faça um algorítmo que exiba em ordem decrescente todos os números pares de 500 até 10 (com while)
"""
i = 500
while i >= 10:
    if i % 2 == 0:
        print(i)
    i -= 1

# ou

i = 500
while i >= 10:
    print(i)
    i -= 2
