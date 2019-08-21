def swapMinMax(L):
    mini = L[0]
    indexmini = 0
    maxi = L[0]
    indexmaxi = 0
    for i in range(1, len(L)):
        if L[i] < mini:
            mini = L[i]
            indexmini = i
        elif L[i] > maxi:
            maxi = L[i]
            indexmaxi = i
    (L[indexmini], L[indexmaxi]) = (L[indexmaxi], L[indexmini])


L = list(map(int, input().split()))
swapMinMax(L)
print(*L)
