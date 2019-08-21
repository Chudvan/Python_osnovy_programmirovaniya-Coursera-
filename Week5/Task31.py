def swapSequence(L):
    for i in range(1, len(L), 2):
        (L[i], L[i - 1]) = (L[i - 1], L[i])


L = list(map(int, input().split()))
swapSequence(L)
print(*L)
