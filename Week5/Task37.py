def printUnique(L):
    uniquelist = []
    blacklist = []
    for i in L:
        if i not in uniquelist:
            uniquelist.append(i)
        else:
            blacklist.append(i)
    for i in uniquelist:
        if i not in blacklist:
            print(i, end=' ')


L = list(map(int, input().split()))
printUnique(L)
