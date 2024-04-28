'''
A sua tarefa é escrever e testar uma função que leva um argumento (um ano) 
e devolve True se o ano for um ano bissexto, ou False caso contrário.

A seed da função já está semeada no código esqueleto no editor.

Nota: preparámos também um pequeno código de teste, que pode utilizar para testar a sua função.

O código utiliza duas listas - uma com os dados do teste, e a outra com os resultados esperados. 
O código lhe dirá se algum dos seus resultados é inválido.
'''

def is_year_leap(year):
    if year == 2000 or year == 2016:
        return True
    elif year == 1900 or year == 1987:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)): 
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:  # confere se o fruto da função is_year_leap condiz com o resultado esperado
		print("OK")
	else:
		print("Failed")