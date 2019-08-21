def isAscending(L):
    cur = L[0]
    i = 1
    length = len(L)
    while i < length:
        if L[i] <= cur:
            return False
        cur = L[i]
        i += 1
    return True


L = list(map(int, input().split()))
if isAscending(L):
    print('YES')
else:
    print('NO')
