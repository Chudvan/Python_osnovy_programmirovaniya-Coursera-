def whoWinner(inFile):
    winnersMarks = [0] * 3
    for line in inFile:
        curLine = line.split()
        curMark = int(curLine[3])
        curClass = int(curLine[2])
        if curMark > winnersMarks[curClass - 9]:
            winnersMarks[curClass - 9] = curMark
    return winnersMarks


inFile = open('input.txt', 'r', encoding='utf-8')
print(*whoWinner(inFile))
