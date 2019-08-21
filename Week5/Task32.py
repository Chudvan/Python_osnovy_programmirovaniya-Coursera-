def cycleShift(L):
    L.insert(0, 1)
    L[0] = L.pop()


L = list(map(int, input().split()))
cycleShift(L)
print(*L)
