def max2(a, b):
    if a > b:
        return b, a
    return a, b


def maxMultiplication(L):
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
    else:
        lastmaxi = L[1]
    for i in range(length):
        if i != indexmini and L[i] < lastmini:
            lastmini = L[i]
        if i != indexmaxi and L[i] > lastmaxi:
            lastmaxi = L[i]
    if mini * lastmini >= maxi * lastmaxi:
        return max2(mini, lastmini)
    return max2(maxi, lastmaxi)


L = list(map(int, input().split()))
print(*maxMultiplication(L))
