def minNotEven(L):
    mini = 0
    for i in range(len(L)):
        if L[i] % 2:
            if not mini:
                mini = L[i]
            elif L[i] < mini:
                mini = L[i]
    return mini


L = list(map(int, input().split()))
print(minNotEven(L))
