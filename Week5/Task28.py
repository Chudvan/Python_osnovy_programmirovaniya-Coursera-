def Nearest(L, x):
    curdifference = abs(L[0] - x)
    cur = L[0]
    for i in L:
        difference = abs(i - x)
        if difference < curdifference:
            curdifference = difference
            cur = i
    return cur


N = int(input())
L = list(map(int, input().split()))
x = int(input())
print(Nearest(L, x))
