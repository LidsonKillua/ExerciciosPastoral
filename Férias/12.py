"""
Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não
haja vencedor deverá ser impressa a palavra EMPATE.
"""

time1 = input('Digite o nome do time 1: ')
time2 = input('Digite o nome do time 2: ')
gols1 = int(input(f'Digite quantos gols o time {time1} fez: '))
gols2 = int(input(f'Digite quantos gols o time {time2} fez: '))

if gols1 > gols2:
    print(f'O time vencedor foi {time1} com {gols1} gols.')
elif gols2 > gols1:
    print(f'O time vencedor foi {time2} com {gols2} gols.')
else:
    print(f'O resultado foi um EMPATE.')
