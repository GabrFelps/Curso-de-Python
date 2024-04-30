#----------------------------------------------------------------------------------------------
'''STRINGS'''
# Example 1
word = 'by'
print(len(word)) #saída: 2

# Example 2
empty = ''
print(len(empty)) #saída: 0

# Example 3
i_am = 'I\'m'
print(len(i_am)) #saída: 3
#----------------------------------------------------------------------------------------------
'''STRINGS MULTILINE'''
multiline = '''Line #1
Line #2'''

print(len(multiline)) # saída: 15 (conta os espaços e a quebra de linha invisível "\n") 
#----------------------------------------------------------------------------------------------
'''OPERAÇÕES COM STRINGS'''
# no geral, strings podem ser:
# concatenadas (+):
str1 = "py"
str2 = "thon"
print(str1 + str2) # saída: python 
# replicadas (*):
print("oi" * 3) # saída: oioioi

# Se quiser saber o valor do code point ASCII/UNICODE de um caratere específico, 
# pode usar uma função chamada ord() (como em ordinal).
print(ord("a")) # saída: 97

# chr():
# a função chr() faz o inverso da ord(), ela pega o valor ASCII/UNICODE e informa
# o seu respectivo caractere
print(chr(ord("a"))) # saída: a

#----------------------------------------------------------------------------------------------
'''SLICES'''
# o comportamento dos slices nas strings é o mesmo que nas tuplas, dicionários e listas...
alpha = "abdefg"
print(alpha[1:3]) # saída: bd
#----------------------------------------------------------------------------------------------
'''STRINGS SÃO IMUTÁVEIS'''
# Isto significa principalmente que a semelhança de strings e listas é limitada. 
# Nem tudo o que se pode fazer com uma lista pode ser feito com uma string.

# A primeira diferença importante não lhe permite utilizar a instrução del 
# para remover qualquer coisa de uma string.

# não possuem o método append() nem o método insert()
#----------------------------------------------------------------------------------------------
'''OPERAÇÕES EM STRINGS'''
# A classe index() (é um método, não uma função) pesquisa a sequência desde o 
# início, a fim de encontrar o primeiro elemento do valor especificado no seu argumento.
print("aAbByYzZaA".index("b")) # saída: 2

# list():
# cria uma lista com cada caractere de uma string
print(list("abcabc")) # saída: ['a', 'b', 'c', 'a', 'b', 'c']

# A classe count() conta todas as ocorrências do elemento dentro da sequência. 
# A ausência de tais elementos não causa problemas.
print("abcabc".count("b")) # saída: 2