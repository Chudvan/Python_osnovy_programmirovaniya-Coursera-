def middleMark(file, numberClasses):
    numberPupils = [0] * numberClasses
    fullMarks = [0] * numberClasses
    for line in file:
        curLine = line.split()
        curClass = int(curLine[2])
        curMark = int(curLine[3])
        numberPupils[curClass - 9] += 1
        fullMarks[curClass - 9] += curMark
    middleMarks = []
    for i in range(numberClasses):
        middleMarks.append(fullMarks[i] / numberPupils[i])
    return middleMarks


file = open('input.txt', 'r', encoding='utf-8')
print(*middleMark(file, 3))
