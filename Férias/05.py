"""
Ler o custo de fábrica de um carro, calcular e escrecer o custo final. 28% distribuidor e 45% impostos
"""

pdistrib = 28
pimpostos = 45
custofab = float(input('Digite o custo de fábrica: '))

# custofab + (custofab * pdistrib / 100) + (custofab * pimpostos / 100) simplificado abaixo
custofinal = custofab + (custofab * (pdistrib + pimpostos))/100

print(f'Com {pdistrib:.1f}% do distribuidor e {pimpostos:.1f}% de impostos o custo final do carro é de R${custofinal:.2f}')
