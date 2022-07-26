"""
Faça um algoritmo para ler dois vetores V1 e V2 de 15 números cada. Calcular e escrever a quantidade de vezes que V1 e
V2 possuem os mesmos números e nas mesmas posições.
"""

V1 = []
V2 = []

for i in range(1, 15 + 1):
    V1.append(int(input(f'Digite o {i}º número da lista 1: ')))
    V2.append(int(input(f'Digite o {i}º número da lista 2: ')))

qtdigual = 0

for i in range(15):
    if V1[i] == V2[i]:
        qtdigual += 1

print(f'A quantidade de números nas mesmas posições é {qtdigual}.')

""" outra forma:

V1 = []
V2 = []
qtdigual = 0

for i in range(1, 15 + 1):
    V1.append(int(input(f'Digite o {i}º número da lista 1: ')))
    V2.append(int(input(f'Digite o {i}º número da lista 2: ')))
    
    if V1[i] == V2[i]:
        qtdigual += 1

print(f'A quantidade de números nas mesmas posições é {qtdigual}.')
"""