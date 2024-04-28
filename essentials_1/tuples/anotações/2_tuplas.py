#-----------------------------------------------------------------------------------------------
'''O QUE É UMA TUPLA?'''
# A primeira e mais clara distinção entre listas e tuples é a sintaxe utilizada para as criar:
# as tuplas usam parentesis, enquanto as listas usam colchetes, embora também seja possível 
# criar um tupla a partir de um conjunto de valores separados por vírgulas.

tupla_1 = (1, 2, 3)
tupla_2 = 1., 2., 3.
print(tupla_1) # saída: (1, 2, 3)
print(tupla_2) # saída: (1.0, 2.0, 3.0)

# cada elemento tuple pode ser de um tipo diferente:
tupla = ("felipe", 17, 1.76, 23)

# porém, por ser imutável, diferentemente de uma lista, a tupla não pode ser alterada
# então qualquer uma dessas tentativas dará erro:
tupla.append(10000)
del tupla[0]
tupla[1] = -10

# a função len() aceita tuples, e devolve o número de elementos contidos no seu interior;
# o operador + pode juntar tuples (já lhe mostrámos isto)
# o operador * pode multiplicar tuples, assim como listas;
# os operadores in e not in trabalham da mesma maneira que nas listas.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2)) # saída: 9
print(t1) # saída: (1, 10, 100, 1000, 10000)
print(t2) # saída: (1, 10, 100, 1, 10, 100, 1, 10, 100)
print(10 in my_tuple) # saída: True
print(-10 not in my_tuple) # saída: True

# Uma das propriedades mais úteis da tuple é o fato de poderem 
# estar a esquerda do sinal de atribuição 
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var) # tuplas aceitam variáveis como elemento, não apenas literais

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3) # saída: (2,) (3, 123) (1,)
#-----------------------------------------------------------------------------------------------



