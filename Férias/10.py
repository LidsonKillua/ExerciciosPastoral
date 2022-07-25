"""
Ler dois valores e escrevê-los em ordem crescente.
"""

val1 = float(input('Escreva o primeiro valor: '))
val2 = float(input('Escreva o segundo valor: '))

if val1 == val2 or val1 < val2:
    menor = val1
    maior = val2
else:
    menor = val2
    maior = val1

print(f'Em ordem crescente eles são: {menor} -> {maior}.')
