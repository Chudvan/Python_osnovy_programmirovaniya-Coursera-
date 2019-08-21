def whichCard(n):
    deck = ' '
    for i in range(n - 1):
        x = input()
        deck += x + ' '
    for i in range(1, n + 1):
        if deck.find(' ' + str(i) + ' ') == -1:
            return i


n = int(input())
print(whichCard(n))
