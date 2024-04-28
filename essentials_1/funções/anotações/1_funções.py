#--------------------------------------------------------------------------------------------------------------
'''DECLARAR UMA FUNÇÃO'''
# corpo da função:
'''
    def function_name():
        function_body 
'''
# Não se deve invocar uma função que não seja conhecida no momento da invocação !!
'''EX:'''

# print("We start here.")
# message()
# print("We end here.")

# def message():
#     print("Enter a value: ")

''' Maneira correta:
    def message():
        print("Enter a value: ")

    print("We start here.")
    message()
    print("We end here.")
'''
#--------------------------------------------------------------------------------------------------------------
'''FUNÇÕES PARAMETRIZADAS'''
# os parâmetros vivem dentro de funções (este é o seu ambiente natural) (funcionam como variáveis)
# os argumentos existem fora de funções, e são portadores de valores passados para parâmetros correspondentes.

def hello(name):    # Definindo a função
    print("Hello,", name)    # Corpo da função

name = input("Enter your name: ") # atribuindo um valor ao parâmetro da função
hello(name)    # chamando a função

# os parametros tambem podem ser passados de outra maneira, sem ser relacionados a sua posição:

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond") # cada parametro foi atribuido ao seu respectivo valor
introduction(last_name = "Skywalker", first_name = "Luke") # não depende da ordem

 # Há como predefinir um parâmetro, caso exista um argumento vazio na chamada de uma função, parece confuso?

def nome(a, b = "Marques"):
    print("Seu nome é:", a, b)

nome("Felipe") # saída: Seu nome é Felipe Marques
# o output acrescentou o "Marques" mesmo eu tendo passado apenas um argumento na chamada da função
# isso acontece porque o segundo parâmetro ja tem um valor definido

nome("Felipe", "Gabriel") # saída: Seu nome é Felipe Gabriel
# isso acontece pois, apesar de o parametro b já estar setado, ele pode ser alterado na chamada da função
#--------------------------------------------------------------------------------------------------------------
'''A INSTRUÇÃO RETURN'''
# return sem expressão:
def happy_new_year(wishes = True): # parâmetro com valor estabelecido (pode ser alterado na chamada da função)
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return # o return não tem nenhuma expressão após ele, então ele só para de executar a função
    
    print("Happy New Year!")

happy_new_year() # chamando a função sem passar argumentos
'''saída:''' 
  # Three...
  # Two...
  # One...
  # Happy New Year!
  
happy_new_year(False) # chamando a função com argumento (mudando o valor do parâmetro que ja estava setado)
'''saída:'''
  # Three...
  # Two...
  # One...

# return com expressão:
def boring_function():
    return 123

x = boring_function()

print("The boring_function has returned:", x) # saída: The boring_function has returned its result. It's: 123

# provoca a terminação imediata da execução da função
# além disso, a função avaliará o valor da expressão e devolvê-la-á como resultado da função.
#--------------------------------------------------------------------------------------------------------------
'''NONE'''
# Os seus dados não representam nenhum valor razoável - na verdade, não é um valor de todo; 
# portanto, não deve tomar parte em nenhuma expressão.

'''Existem apenas dois tipos de circunstâncias onde None pode ser utilizado em segurança:'''
# quando o atribui a uma variável (ou o devolve como o resultado de uma função)
# quando o compara com uma variável para diagnosticar o seu estado interno.
value = None
if value is None:
    print("Sorry, you don't carry any value")

def strange_function(n): # função para ver se um número é par
    if(n % 2 == 0):
        return True
print(strange_function(2)) # retorna True
print(strange_function(1)) # retorna None
#--------------------------------------------------------------------------------------------------------------
'''LISTAS E FUNÇÕES'''
def list_sum(lst): # função que soma elementos de uma lista
    s = 0 # soma inicialmente vazia
    
    for elem in lst: # para cada elemento na lista
        s += elem # a sua soma é incrementada em uma variável
    
    return s
print(list_sum([5, 4, 3])) # saída: 12

def strange_list_fun(n): # função que gera uma lista com n elementos 
    strange_list = [] # lista inicialmente vazia
    
    for i in range(0, n): # para cada i no range do tamanho da lista desejada
        strange_list.insert(0, i) # insere esse i no index 0 da lista
    
    return strange_list # retorna a lista

print(strange_list_fun(5)) # saída: [4, 3, 2, 1, 0]
#--------------------------------------------------------------------------------------------------------------
'''KEYWORD GLOBAL'''
# pode alargar o scope de uma variável de forma a incluir os corpos das funções
global variable 
# agora qualquer parte do código pode acessar a variável

def my_function():
    global var # global definido dentro da função 
    var = 2 # será esse valor pra todo o resto do código
    print("Do I know that variable?", var)

var = 1 # mesmo alterando o valor, o da função é o que conta
my_function()
print(var)
'''extra:'''
# dê uma olhada na forma como o símbolo da barra invertida (\) é usado. 
# Se o utilizar em código Python e terminar uma linha com ele, 
# dirá ao Python para continuar a linha de código na próxima linha de código.

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
#--------------------------------------------------------------------------------------------------------------
'''RECURSIVIDADE'''
# é uma técnica em que a função invoca a si própria:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2) # invocando a sí própria

# Pode usar funções recursivas em Python para escrever um código limpo e elegante,
# e dividi-lo em pedaços mais pequenos e organizados. Por outro lado, é preciso ter muito cuidado,
# pois pode ser fácil cometer um erro e criar uma função que nunca termina.
# Também é preciso lembrar que as chamadas recursivas consomem muita memória,
# e por isso podem por vezes ser ineficientes.
#--------------------------------------------------------------------------------------------------------------




