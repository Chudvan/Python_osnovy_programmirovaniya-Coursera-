def whichMore():
    L = list(map(int, input().split()))
    cur = L[0]
    S = []
    for i in range(1, len(L)):
        if L[i] > cur:
            S.append(L[i])
        cur = L[i]
    return S


print(*whichMore())
