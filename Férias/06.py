"""
As maçãs custam 1,30 cada se forem compradas menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Leia o número
de maçãs compradas, calcule e escreva o total da compra.
"""

vvarejo = 1.3
vatacado = 1
qtdatacado = 12
vtotal = 0

qtdmacas = int(input('Digite a quantidade de macãs: '))

if qtdmacas >= qtdatacado:
    vtotal = qtdmacas * vatacado
else:
    vtotal = qtdmacas * vvarejo

print(f'O total da compra foi de R${vtotal:.2f}.')
