inFile = open('input.txt')
wordCountDict = dict()
wordList = []
for line in inFile:
    lineList = line.split()
    for word in lineList:
        if word not in wordCountDict:
            wordCountDict[word] = 0
        wordCountDict[word] += 1
        wordList.append(wordCountDict[word] - 1)
print(*wordList)
