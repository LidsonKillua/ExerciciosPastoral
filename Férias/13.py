"""
Ler 10 valores e escrever quantos desses estão no intervalo [10,20] e quantos estão fora
"""

noint = 0
fora = 0

for i in range(1, 11):
    num = float(input(f'Digite o {i}º valor: '))

    if 10 <= num <= 20:
        noint += 1
    else:
        fora += 1

print(f'Dos números passados {noint} estão dentro do intervalo e {fora} estão fora.')
