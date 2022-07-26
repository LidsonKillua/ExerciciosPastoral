"""
Escreva um algoritmo para ler 10 números, todos os números lidos com valor inferior a 40 devem ser somados
"""

soma = 0
for i in range(1, 11):
    num = float(input(f'Digite o {i}º valor: '))

    if num < 40:
        soma += num

print(f'A soma dos números passados menores que 40 é = {soma:.2f}.')
