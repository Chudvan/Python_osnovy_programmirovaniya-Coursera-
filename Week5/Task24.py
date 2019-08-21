def printReverse(L):
    for i in range(len(L) - 1, -1, -1):
        print(L[i], end=' ')


L = list(map(int, input().split()))
printReverse(L)
