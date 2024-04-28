palpite = [5, 11, 9, 42, 3, 49]
sorteio = [3, 7, 11, 42, 34, 49]
acertos = 0

for number in sorteio:
    if number in sorteio:
        acertos += 1

print(acertos)