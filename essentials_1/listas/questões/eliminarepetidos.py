my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

for i in my_list:
    if my_list[i] in my_list[1:len(my_list)]:
        del my_list[i]
#
print("The list with unique elements only:")
print(my_list)
