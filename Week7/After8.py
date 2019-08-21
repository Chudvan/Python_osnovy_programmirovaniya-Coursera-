from sys import stdin


def number(numberPhone):
    numberPhone = numberPhone.strip()
    numberNormal = ''.join(numberPhone.split('-'))
    firstSym = numberNormal[0]
    numberList = numberNormal.split('(')
    if len(numberList) == 2:
        codeAndNumber = numberList[1].split(')')
        numberList[1] = codeAndNumber[0]
        numberList.append(codeAndNumber[1])
    elif firstSym == '+':
        numberList.append(numberNormal[2:5])
        numberList.append(numberNormal[5:])
    elif firstSym == '8':
        numberList.append(numberNormal[1:4])
        numberList.append(numberNormal[4:])
    else:
        numberList.append('495')
        numberList.append(numberNormal)
    numberList[0] = '8'
    return numberList


numberVasya = stdin.readline()
numberVasya = number(numberVasya)
strNumberDict = dict()
i = 1
for line in stdin:
    strNumberDict[i] = (line.strip(), number(line))
    i += 1
for j in range(1, i):
    if strNumberDict[j][1] == numberVasya:
        print('YES')
    else:
        print('NO')
