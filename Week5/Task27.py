def insertElement(L, M):
    L.append(1)
    k = M[0]
    for i in range(len(L) - 1, k, -1):
        L[i] = L[i - 1]
    L[k] = M[1]


L = list(map(int, input().split()))
M = list(map(int, input().split()))
insertElement(L, M)
print(*L)
