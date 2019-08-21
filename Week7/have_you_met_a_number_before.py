L = list(map(int, input().split()))
M = set()
for element in L:
    if element not in M:
        M.add(element)
        print('NO')
    else:
        print('YES')
