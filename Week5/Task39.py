def isUnique(L):
    if len(L) == len(set(L)):
        return True
    return False


def isKillQueen():
    xPoition = []   # Первая координата
    yPosition = []   # Вторая координата
    firstDiagonal = []  # Список с первой(тривиальной) нумерацией диагоналей
    secondDiagonal = []   # Список со второй(обратнойной) нумерацией диагоналей
    for i in range(8):
        x, y = map(int, input().split())
        xPoition.append(x)
        yPosition.append(y)
        numberFirstDiag = x - y
        firstDiagonal.append(numberFirstDiag)
        numberSecondDiag = (9 - x) - y
        secondDiagonal.append(numberSecondDiag)
    if isUnique(xPoition) and isUnique(yPosition):
        # Проверка на отсутсвие совпадений в каждом из списков
        if isUnique(firstDiagonal) and isUnique(secondDiagonal):
            return False
            # Если совпадений нет, значит ферзи не бьют друг друга
        return True
    return True


if isKillQueen():
    print('YES')
else:
    print('NO')
