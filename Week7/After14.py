from sys import stdin
numberWordsDict = dict()
for line in stdin:
    lineList = line.split()
    for word in lineList:
        if word not in numberWordsDict:
            numberWordsDict[word] = 0
        numberWordsDict[word] += 1
tupleList = []
for word in numberWordsDict:
    tupleList.append((numberWordsDict[word], word))
tupleList.sort(key=lambda curTuple: (-curTuple[0], curTuple[1]))
for curTuple in tupleList:
    print(curTuple[1])
