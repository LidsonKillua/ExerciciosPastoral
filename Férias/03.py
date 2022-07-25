"""
Ler o total de eleitores de um município, votos brancos, nulos e válidos.
Calcular o percentual que cada um representa em relação ao total
"""

eleitores = int(input('Digite o total de eleitores: '))
vtotal = int(input('Digite o total de votos: '))
vbrancos = int(input('Digite o total de votos brancos: '))
vnulos = int(input('Digite o total de votos nulos: '))
vvalidos = vtotal - vbrancos - vnulos

ptotal = vtotal * 100 / eleitores
pbrancos = vbrancos * 100 / eleitores
pnulos = vnulos * 100 / eleitores
pvalidos = vvalidos * 100 / eleitores

print(f'{ptotal:.2f}% de {eleitores} eleitores votaram, totalizando {vtotal} votos.')
print(f'De todas as pessoas apenas {pvalidos:.2f}% foram votos válidos.')
print(f'Houveram também {pbrancos:.2f}% de votos brancos, e {pnulos:.2f}% de votos nulos.')
