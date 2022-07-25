"""
Ler a idade em anos, meses e dias e escrever apenas em dias(ano = 365 , mês = 30 dias)
"""

anos = int(input('Quantos anos você tem? '))
meses = int(input('Além disso, mais quantos meses? '))
dias = int(input('Além disso, mais quantos dias? '))

diastotais = anos * 365 + meses * 30 + dias

print(f'Você nasceu a {diastotais} dias no total.')
