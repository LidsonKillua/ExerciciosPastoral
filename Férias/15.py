"""
Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos (incluindo eles).
"""

val1 = int(input('Digite o primeiro valor: '))
val2 = int(input('Digite o segundo valor: '))
soma = 0

if val2 > val1:
    for i in range(val1, val2 + 1):
        soma += i

print(f'A soma dos valores inteiros entre {val1} e {val2} é igual a {soma}.')
