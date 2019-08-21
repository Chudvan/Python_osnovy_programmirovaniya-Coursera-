def howManyWinners(inFile):
    winnersMarks = [0] * 3
    numberOfWinners = [0] * 3
    for line in inFile:
        curLine = line.split()
        curMark = int(curLine[3])
        curClass = int(curLine[2])
        if curMark > winnersMarks[curClass - 9]:
            winnersMarks[curClass - 9] = curMark
            numberOfWinners[curClass - 9] = 1
        elif curMark == winnersMarks[curClass - 9]:
            numberOfWinners[curClass - 9] += 1
    return numberOfWinners


inFile = open('input.txt', 'r', encoding='utf-8')
print(*howManyWinners(inFile))
