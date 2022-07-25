"""
Ler as notas da primeira e segunda avaliações de um aluno. Calcular a média e escrever se ele foi ou não aprovado
(média >= 6)
"""

p1 = float(input('Digite a nota da prova 1: '))
p2 = float(input('Digite a nota da prova 2: '))

media = (p1 + p2) / 2

if media >= 6:
    resultado = 'APROVADO'
else:
    resultado = 'REPROVADO'

print(f'A média das suas provas foi {media:.2f}, você foi {resultado}!')
