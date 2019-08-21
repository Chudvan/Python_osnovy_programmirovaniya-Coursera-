def reverse(L):
    length = len(L)
    for i in range((length - 1) // 2 + 1):
        (L[i], L[length - 1 - i]) = (L[length - 1 - i], L[i])
    return L


L = list(map(int, input().split()))
print(*reverse(L))
