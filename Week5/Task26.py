def deleteElement(L, k):
    length = len(L)
    for i in range(k, length - 1):
        L[i] = L[i + 1]
    L.pop()


L = list(map(int, input().split()))
k = int(input())
deleteElement(L, k)
print(*L)
