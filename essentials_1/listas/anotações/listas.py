# Os elementos numa lista são sempre numerados a partir do zero:
#          0  1   2   3   4
numbers = [1, 2, 10, 15, 21]

# Variáveis em que se atribui mais de um valor, podem ser chamadas de listas
# A quantidade de elementos N dentro de uma lista é o seu comprimento (ex: 5)
#-------------------------------------------------------------------------------------
# Os elementos dentro de uma lista podem ter tipos diferentes
# Alguns deles podem ser inteiros, outros floats, e outros ainda podem ser listas. 

lista = ['felipe', 17, 2.5, numbers]
#-------------------------------------------------------------------------------------
'''INDEXAR LISTAS'''
#  alterar elementos em uma lista já setada:

numeros = [1, 16, 32, 64, 128]
numeros[0] = 123 # insere um novo valor ao index 0
# nova lista: [123, 16, 32, 64, 128]

numeros[2] = numeros[4] # transforma o valor do index 2 no valor do index 4
# nova lista: [123, 16, 129, 64, 128]
#-------------------------------------------------------------------------------------
'''ACESSAR ELEMENTOS DA LISTA'''
#  printar elementos da lista:

print(numeros) # saída: [123, 16, 128, 64, 128]
print(numeros[0]) # saída: 123
print(len(numeros)) # saída: 5 (tamanho da lista)
#-------------------------------------------------------------------------------------
'''REMOVER ELEMENTOS DE UMA LISTA'''
#  instrução del:

del numeros[0] # deleta o elemento do index 0 da lista
print(numeros) #saída: [16, 128, 64, 128]
#-------------------------------------------------------------------------------------
'''INDICES NEGATIVOS'''
# indices negativos indicam do último ao primeiro elemento da lista:

print(numeros[-1]) # saída: 128
#-------------------------------------------------------------------------------------
'''ADICIONAR ELEMENTOS EM UMA LISTA, COM MÉTODOS'''
# append:
numeros.append(256) # adiciona o valor passado no argumento a lista, na última posição
# nova lista: [16, 128, 64, 128, 256]

#insert:
numeros.insert(1,32) # adiciona o valor no index (posição, valor)
# nova lista: [16, 32, 128, 64, 128, 256]
#-------------------------------------------------------------------------------------
'''SOMAR ELEMENTOS DA LISTA'''
my_list = [10, 1, 8, 3, 5] #lista
total = 0 # variável  a qual será atribuida a soma dentro do loop

for i in my_list:  # para cada elemento na lista
    total += i     # soma dos elementos atribuidos na variável a cada volta no loop

print(total) # soma total da lista (27)
#-------------------------------------------------------------------------------------
'''TROCAR ELEMENTOS DE UMA LISTA ENTRE SI'''
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0] # inverte valores dos index 0 e 4 
my_list[1], my_list[3] = my_list[3], my_list[1] # inverte valores dos index 1 e 3

print(my_list) # saída: [5, 3, 8 , 1, 10]
#-------------------------------------------------------------------------------------
'''ORGANIZAR LISTA DE MANEIRA CRESCENTE'''
my_list = [8, 10, 6, 2, 4]  
trocou = True  # Atribuição pra entrar no loop

while trocou:
    trocou = False  # Nenhuma troca foi feita até o momento
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            trocou = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list) # saída: [2, 4, 6, 8, 10] 

'''ouu'''

my_list.sort()
print(my_list) # saída: [2, 4, 6, 8, 10] 
# bonûs:
my_list.reverse() # saída: [10, 8, 6, 4, 2](inverte os elementos da lista)
#-------------------------------------------------------------------------------------
'''A VIDA INTERNA DAS LISTAS'''
# o nome de uma variável ordinária é o nome do seu conteúdo;
# o nome de uma lista é o nome de um local de memória onde a lista é armazenada.
lista_1 = [1]
lista_2 = lista_1
lista_1[0] = 12
print(lista_2) 
# a saída desse print será 12, e não 1, pois a partir de "lista_2 = lista_1" ambas
# ocuparão o mesmo espaço na memória e modificar um deles afeta o outro.
#-------------------------------------------------------------------------------------
'''SLICES'''
# uma maneira de modificar o comportamento previamente apresentado é utilizando slices
lista_2 = lista_1[:] # o slice vai fazer uma cópia da lista em outro espaço da memoria

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] # vai fazer a cópia com os index 1 à 3(não inclusivo)
print(new_list) # saída: [8, 6]

# my_list[start:end]
# start é o index do primeiro elemento incluído no slice;
# end é o index do primeiro elemento não incluído no slice.
# my_list[:end] = my_list[0:end]
# instrução del tambem aceita o slice:

del my_list[0:2]
print(my_list) # saída: [4, 2]
#-------------------------------------------------------------------------------------
'''OPERADORES IN E NOT IN'''
#elem in my_list
#elem not in my_list
print(2 in my_list) # saída: True
print(2 not in my_list) # saída: False 
print(12 in my_list) # saída: False
print(12 not in my_list) # saída: True

# O primeiro deles (in) verifica se um dado elemento (o seu argumento da esquerda) 
# está atualmente armazenado algures dentro da lista (o argumento da direita) - 
# o operador devolve True neste caso.

# O segundo (not in) verifica se um dado elemento (o seu argumento da esquerda) 
# está ausente numa lista - o operador devolve True neste caso.
#-------------------------------------------------------------------------------------
'''COMPREENSÃO DE LISTA'''
squares = [x ** 2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 81]
# a linha acima é uma maneira simplificada de:
squares = []
for x in squares:
    squares.append(x**2)
#-------------------------------------------------------------------------------------
'''ARRAY BIDIMENSIONAL'''
# vamos fazer um tabuleiro de xadrez:
board = []

for i in range(8): # repete 8 vezes 8 loops resultando em 64 espaços vazios
    row = ["empty" for i in range(8)] # empty é uma representação figurativa do vazio
    board.append(row) 
# o código "gera" 64 espaços vazios, simulado um tabuleiro de xadrez
# a variável board é agora um array bidimensional 
# também é chamada, por analogia aos termos algébricos, uma matriz.
#-------------------------------------------------------------------------------------