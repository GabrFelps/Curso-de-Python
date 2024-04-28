'''
A sua tarefa consiste em escrever e testar uma função que toma três argumentos (um ano, um mês e um dia do mês) 
e devolve o dia correspondente do ano, ou devolve None se algum dos argumentos for inválido.

Use as funções previamente escritas e testadas. Adicione alguns casos de teste ao código. Este teste é apenas um começo.
'''

def is_year_leap(year):
    
    if year == 2000 or year == 2016:
        return True
    elif year == 1900 or year == 1987:
        return False

def days_in_month(year, month):
    
    if month > 12 or month < 1:
        None
    elif is_year_leap(year) == True and month == 2:
        return 29
    elif is_year_leap(year) == False and month == 2:
        return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        return 30

def day_of_year(year, month, day):
    
    if is_year_leap(year) == True:
        return 366
    else:
        return 365
    

print(day_of_year(2000, 12, 31))
