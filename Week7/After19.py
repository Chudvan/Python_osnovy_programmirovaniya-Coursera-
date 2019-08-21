from sys import stdin


def accent(char):
    if char.isupper():
        return 1
    return 0


n = int(input())
dictionary = dict()
for i in range(n):
    line = (stdin.readline()).strip()
    lowerWord = line.lower()
    if lowerWord not in dictionary:
        dictionary[lowerWord] = set()
    dictionary[lowerWord].add(line)
petyaText = stdin.readline()
listWords = petyaText.split()
mistakes = 0
for word in listWords:
    lowerWord = word.lower()
    if lowerWord not in dictionary:
        numberAccents = sum(map(accent, list(word)))
        if numberAccents != 1:
            mistakes += 1
    elif word not in dictionary[lowerWord]:
        mistakes += 1
print(mistakes)
