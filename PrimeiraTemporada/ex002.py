"""
Construa um algorítmo que pede para o usuário digitar dois números e exiba o primeiro elevado ao segundo:
"""
import math

num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))

print(f'{num1} elevado a {num2} = {math.pow(num1, num2)}')

# ou
# print(f'{num1} elevado a {num2} = {num1**num2}')
