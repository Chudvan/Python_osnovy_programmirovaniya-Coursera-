from sys import stdin
numberWordsDict = dict()
maxNumber = 0
for line in stdin:
    lineList = line.split()
    for word in lineList:
        if word not in numberWordsDict:
            numberWordsDict[word] = 0
        numberWordsDict[word] += 1
        if numberWordsDict[word] > maxNumber:
            maxNumber = numberWordsDict[word]
mostFrequencyWord = ''
for word in numberWordsDict:
    if numberWordsDict[word] == maxNumber:
        if mostFrequencyWord == '':
            mostFrequencyWord = word
        elif word < mostFrequencyWord:
            mostFrequencyWord = word
print(mostFrequencyWord)
