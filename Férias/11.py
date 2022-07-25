"""
Ler a hora de início e a hora de fim de um jogo de Xadrez(horas inteiras) e calcule a duração do jogo em horas, sabendo
que a duração máxima do jogo é de 24h e ele pode iniciar em um dia e terminar no outro.
"""

hi = int(input('Digite a hora de início do jogo: '))
hf = int(input('Digite a hora de fim do jogo: '))
tjogo = 0

if hf > hi:
    tjogo = hf - hi
elif hf == hi:
    tjogo = 1
else:
    tjogo += 24-hi
    tjogo += hf

if tjogo > 24:
    print('Informe dados válidos')
else:
    print(f'O tempo total de jogo foi de {tjogo}h.')
