"""
Ler salário, percentual de reajuste e escrever novo salário
"""

salario = float(input('Digite o salário atual: '))
reaj = float(input('Qual a porcentagem de reajuste? '))
novosalario = salario + (salario * reaj / 100)

print(f'Seu salario de R${salario:.2f} com reajuste de {reaj:.2f}% agora é de R${novosalario:.2f}')
