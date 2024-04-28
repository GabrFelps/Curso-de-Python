#-------------------------------------------------------------------------------------------------------------------------------
'''O QUE SÃO MÓDULOS?'''
# um ficheiro contendo definições e declarações Python, que pode ser posteriormente importado e utilizado quando necessário.
# duas maneiras de utilizar módulos

# o primeiro (provavelmente o mais comum) acontece quando se pretende utilizar um módulo já existente, escrito por outra pessoa, 
# ou criado por si próprio durante o seu trabalho nalgum projeto complexo - neste caso você é o utilizador do módulo;

# o segundo ocorre quando se pretende criar um novo módulo, quer para uso próprio, 
# quer para facilitar a vida a outros programadores - você é o fornecedor do módulo.

# Cada módulo consiste em entidades (como um livro consiste em capítulos). 
# Estas entidades podem ser funções, variáveis, constantes, classes e objetos. 
# Se souber como aceder a um determinado módulo, pode fazer uso de qualquer uma das entidades que ele armazena
#-------------------------------------------------------------------------------------------------------------------------------
'''IMPORTAR UM MÓDULO'''
# utilizando o método import
import math
print(math.sin(math.pi/2)) #saída: 1.0  

from math import pi # importa apenas uma entidade do módulo

import time as t # importa um módulo e renomeia ele
t.sleep(1) # nova maneira de utilizar o módulo

from math import pi as PI, sin as sine # renomeia a entidade do módulo
print(sine(PI/2)) 
import os 
print(dir(os)) # A função devolve uma lista ordenada alfabeticamente contendo todos os nomes de entidades disponíveis no módulo
# saída:

# ['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 
#  'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 
#  'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 
#  'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__', '__builtins__', '__doc__', 
#  '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods', '_execvpe', '_exists', '_exit', 
#  '_fspath', '_get_exports_list', '_wrap_close', 'abc', 'abort', 'access', 'add_dll_directory', 'altsep', 'chdir', 
#  'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 
#  'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', ... 

import platform

print(platform.platform())  #permite-lhe aceder aos dados da plataforma subjacente, ou seja, hardware, sistema operativo,
# e informação da versão do intérprete.

print(platform.machine()) # nome genérico do processador que executa o seu SO

print(platform.processor()) # nome do processador damáquina
print(platform.system()) # devolve o nome genérico do SO como uma cadeia.


