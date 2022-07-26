"""
Uma loja está levantando o valor total de todas as mercadorias em estoque. Escreva um algoritmo que permita a entrada
das seguintes informações:
    a) O número total de mercadorias no estoque
    b) O valor de cada mercadoria.
Ao final imprimir o valor total em estoque e a média de valor das mercadorias
"""

mercadorias = []
temp = []

escolha = 's'
while escolha[0] not in 'Nn':
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor: '))
    temp.append(produto)
    temp.append(valor)
    mercadorias.append(temp[:])
    temp.clear()

    escolha = input('Deseja adicionar mais um produto? [S/N] ')

vtotal = media = 0

for produto in mercadorias:
    vtotal += produto[1]

media = vtotal/len(mercadorias)

print(f'O valor total em estoque é de R${vtotal:.2f} e a média do valor das mercadorias é R${media:.2f}')

print()
print('Tabela adicional:')

for i in mercadorias:
    print(f'{i[0]:<40} R${i[1]:5.2f}')
