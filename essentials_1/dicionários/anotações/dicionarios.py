#----------------------------------------------------------------------------------------------------------------------
'''O QUE É UM DICIONÁRIO?'''

# O dicionário é outra estrutura de dados Python. Não é um tipo de sequência 
# (mas pode ser facilmente adaptado ao processamento de sequências) e é mutável.

# O dicionário python funciona da mesma maneira que um dícionário bilíngue, mas como assim ?
# se eu procurar a palavra knowledgeable no dicionário inglês-português encontrarei "conhecedor" como tradução

# No mundo de Python, a palavra que se procura chama-se key. A palavra que obtém do dicionário chama-se um value.
# então o dicionário é um conjunto de key-values

# cada chave deve ser única - não é possível ter mais do que uma chave com o mesmo valor;
# uma chave pode ser qualquer tipo de objeto imutável: pode ser um número (inteiro ou float),
# ou mesmo uma string, mas não uma lista;
# um dicionário não é uma lista - uma lista contém um conjunto de valores numerados, 
# enquanto que um dicionário contém pares de valores;
# a função len() funciona também para dicionários - devolve o número de elementos de key-value no dicionário;
# um dicionário é uma ferramenta de sentido único - se tiver um dicionário inglês-francês, 
# pode procurar por equivalentes franceses de termos ingleses, mas não vice-versa.
#------------------------------------------------------------------------------------------------------------------------
'''COMO FAZER UM DICIONÁRIO?'''

dictionary = {"cat": "gato", "dog": "cachorro", "horse": "cavalo"}
phone_numbers = {'Felipe': 5551234567, 'Ingrid': 22657854310}
empty_dictionary = {}

print(dictionary) # {'cat': 'gato', 'dog': 'cachorro', 'horse': 'cavalo'}
print(phone_numbers) # {'Felipe': 5551234567, 'Ingrid': 22657854310}
print(empty_dictionary) # {}
#------------------------------------------------------------------------------------------------------------------------
'''COMO USAR UM DICIONÁRIO?'''

print(dictionary['cat']) # saída: gato
print(phone_numbers['Ingrid']) # saída: 22657854310


dictionary = {"cat": "gato", "dog": "cachorro", "horse": "cavalo"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")
# saída:
# cat -> gato
# lion is not in dictionary
# horse -> cavalo
#------------------------------------------------------------------------------------------------------------------------
'''COMO ADAPTAR UM DICIONÁRIO AO LOOP FOR?'''
# utilizando o metodo keys:
# O método devolve um objeto iterável que consiste em todas as chaves recolhidas dentro do dicionário. 
# Ter um grupo de chaves permite-lhe aceder a todo o dicionário de uma forma fácil e prática.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
# saída:
# horse -> cheval
# dog -> chien
# cat -> chat

# utilizando o metodo sorted:
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key]) # "horse", "->", dicionary[horse]...
# saída:
# horse -> cheval
# dog -> chien
# cat -> chat

# utilizando o método itens:
# O método devolve tuples (este é o primeiro exemplo onde os tuples são algo mais do que apenas um exemplo de si mesmos)
# onde cada tuple é um par key-value.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)
# saída:
# horse -> cheval
# dog -> chien
# cat -> chat

# utilizando método values:
# funciona de forma semelhante a keys(), mas devolve valores.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for french in dictionary.values():
    print(french)
# saída:
# cheval
# chien
# chat
#------------------------------------------------------------------------------------------------------------------------
'''ADICIONAR E MODIFICAR VALORES EM UM DICIONÁRIO'''

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou' # atribui um novo valor à key 'cat'
print(dictionary) # saída: {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}

# adicionar uma nova chave:
# update() -> adiciona uma key e valor

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne' # adicionando chave atualmente inexistente e seu valor
print(dictionary) # saída: {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}

# remover uma chave 
# popitem() -> remove a ultima key junto com seu valor

del dictionary["cat"]
print(dictionary) # saída: {'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'}
#------------------------------------------------------------------------------------------------------------------------
'''TUPLES E DICIONÁRIOS TRABALHANDO JUNTOS'''

school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break

if name in school_class:
        school_class[name] += (score,)
else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

