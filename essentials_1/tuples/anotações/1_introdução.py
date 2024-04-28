#-----------------------------------------------------------------------------------------------------------
'''TIPOS DE SEQUÊNCIA E MUTABILIDADE'''
'''sequência:'''
# Um tipo de sequência é um tipo de dados em Python que é capaz de armazenar mais de um valor 
# (ou menos de um, pois uma sequência pode estar vazia), e estes valores podem ser pesquisados 
# sequencialmente (daí o nome), elemento a elemento.

# Como o loop for é uma ferramenta especialmente concebida para iterar através de sequências, 
# podemos expressar a definição como: uma sequência é um dado que pode ser analisado pelo loop for .

#ex: 
lista = [1, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
'''mutabilidade:'''
# a mutabilidade - é uma propriedade de qualquer dado Python que descreve a sua disponibilidade 
# para ser livremente alterado durante a execução do programa.
# Existem dois tipos de dados Python: mutáveis e imutáveis.

# Os dados MUTÁVEIS podem ser atualizados livremente a qualquer momento - chamamos esta operação in situ.

# In situ é uma frase em latim que se traduz literalmente para no local. 
# Por exemplo, a instrução a seguir modifica os dados in situ:
lista.append(63)

# Dados IMUTÁVEIS não podem ser modificados desta maneira.

# Imagine que uma lista só pode ser atribuída e lida. 
# Não seria possível anexar-lhe um elemento, nem remover qualquer elemento da mesma. 
# Isto significa que anexar um elemento ao fim da lista exigiria a recriação da lista a partir do zero.
# Teria de construir uma lista completamente nova, constituída por todos os elementos da lista já existente,
# mais o novo elemento. 

#ex: TUPLAS
# mas o que são tuplas? é o que veremos agora.
#-----------------------------------------------------------------------------------------------------------