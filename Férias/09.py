"""
Ler dois valores e escrever o maior deles
"""

val1 = float(input('Escreva o primeiro valor: '))
val2 = float(input('Escreva o segundo valor: '))

if val1 == val2:
    print(f'{val1} é igual a {val2}.')
elif val1 > val2:
    print(f'{val1} é maior que {val2}.')
else:
    print(f'{val1} é menor que {val2}.')
