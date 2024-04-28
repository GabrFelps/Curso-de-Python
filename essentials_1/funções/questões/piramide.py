blocks = int(input("Enter the number of blocks: "))
countanterior = 1
countatual = 1
countrazao = 0
height = 0


while countanterior <= blocks:
    countanterior = countatual + 2 + countrazao
    # 1 3 6 10 15 21 28
    height += 1
    countrazao += 1
    countatual = countanterior

print("The height of the pyramid:", height)