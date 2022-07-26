"""
Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada
das seguintes informações:
    a) O número total de mercadorias no estoque
    b) O valor de cada mercadoria.
Ao final imprimir o valor total em estoque e a média de valor das mercadorias
"""

mercadorias = []
temp = []

qtdmerc = int(input('Quantos produtos você quer adicionar? '))
for i in range(1, qtdmerc + 1):
    produto = input(f'Digite o nome do {i}º produto: ')
    valor = float(input('Digite o valor: '))
    temp.append(produto)
    temp.append(valor)
    mercadorias.append(temp[:])
    temp.clear()

vtotal = media = 0

for produto in mercadorias:
    vtotal += produto[1]

media = vtotal/len(mercadorias)

print(f'O valor total em estoque é de R${vtotal:.2f} e a média do valor das mercadorias é R${media:.2f}')
