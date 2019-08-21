def minPositive(L):
    mini = 1001
    for i in range(len(L)):
        if L[i] > 0 and L[i] < mini:
            mini = L[i]
    return mini


L = list(map(int, input().split()))
print(minPositive(L))
