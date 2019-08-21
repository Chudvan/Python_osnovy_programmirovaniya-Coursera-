def whichSecondMax(inFile):
    maxMark = [0] * 3
    secondMax = [0] * 3
    for line in inFile:
        cur = line.split()
        curClass = int(cur[2])
        curMark = int(cur[3])
        i = curClass - 9
        if maxMark[i] < curMark:
            secondMax[i] = maxMark[i]
            maxMark[i] = curMark
        elif maxMark[i] > curMark and secondMax[i] < curMark:
            secondMax[i] = curMark
    for curClass in range(3):
        print(secondMax[curClass], end=' ')


inFile = open('input.txt', 'r', encoding='utf-8')
whichSecondMax(inFile)
