"""
A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. faça um algoritmo para coletar dados sobre o
salário e número de filhos de cada habitante e após as leituras, escrever:
    a) Média de salário
    b) Média de número de filhos
    c) Maior salário
    d) Percentual de pessoas com salário menor que 150,00
O final das entradas se dá com um salário negativo
"""

pessoas = []
temp = []

escolha = 's'
while True:
    salario = float(input('Digite o salário (<0 para terminar): '))

    if salario < 0:
        break

    nfilhos = int(input('Digite a quantidade de filhos: '))
    temp.append(salario)
    temp.append(nfilhos)
    pessoas.append(temp[:])
    temp.clear()


somaf = somas = qtdabaixo = maiors = 0
for i in pessoas:
    somas += i[0]
    somaf += i[1]

    if i[0] < 150:
        qtdabaixo += 1

    if i[0] > maiors:
        maiors = i[0]

medias = somas / len(pessoas)
mediaf = somaf / len(pessoas)
pabaixo = qtdabaixo * len(pessoas) / 100

print(f'A média de salário é R${medias:.2f}, a média de filhos é {mediaf:.1f} filhos por pessoa')
print(f'O maior salário é de R${maiors:.2f} e a quantidade de pessoas com salário menor que RS150,00 é {qtdabaixo}.')
