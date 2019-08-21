def max3(a, b, c):
    a, b = max2(a, b)
    b, c = max2(b, c)
    a, b = max2(a, b)
    return a, b, c


def max2(a, b):
    if a > b:
        return b, a
    return a, b


def maxMultiplication3(L):
    mini = L[0]
    indexmini = 0
    maxi = L[0]
    indexmaxi = 0
    length = len(L)
    for i in range(1, length):
        if L[i] < mini:
            mini = L[i]
            indexmini = i
        elif L[i] > maxi:
            maxi = L[i]
            indexmaxi = i
    if 0 != indexmini:
        lastmini = L[0]
    else:
        lastmini = L[1]
    if 0 != indexmaxi:
        lastmaxi = L[0]
        indexlastmaxi = 0
    else:
        lastmaxi = L[1]
        indexlastmaxi = 1
    for i in range(length):
        if i != indexmini and L[i] < lastmini:
            lastmini = L[i]
        if i != indexmaxi and L[i] > lastmaxi:
            lastmaxi = L[i]
            indexlastmaxi = i
    if 0 != indexmaxi and 0 != indexlastmaxi:
        thirdmaxi = L[0]
    elif 1 != indexmaxi and 1 != indexlastmaxi:
        thirdmaxi = L[1]
    elif 2 != indexmaxi and 2 != indexlastmaxi:
        thirdmaxi = L[2]
    for i in range(length):
        if i != indexmaxi and i != indexlastmaxi and L[i] > thirdmaxi:
            thirdmaxi = L[i]
    if mini * lastmini * maxi >= maxi * lastmaxi * thirdmaxi:
        return max3(mini, lastmini, maxi)
    return max3(maxi, lastmaxi, thirdmaxi)


L = list(map(int, input().split()))
print(*maxMultiplication3(L))
