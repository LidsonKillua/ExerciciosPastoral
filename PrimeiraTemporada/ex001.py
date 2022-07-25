"""
Contrua um algoritmo que peça ao usuário para digitar duas palavras e verifique se elas começam ou terminam com o mesmo caracter
"""

word1 = input('Digite uma palavra: ')
word2 = input('Digite outra palavra: ')

if word1[0].upper() == word2[0].upper():
    print('As duas palavras começam com a mesma letra')
else:
    print('As duas palavras não começam com a mesma letra')

if word1[-1].upper() == word2[-1].upper():
    print('As duas palavras terminam com a mesma letra')
else:
    print('As duas palavras não terminam com a mesma letra')
