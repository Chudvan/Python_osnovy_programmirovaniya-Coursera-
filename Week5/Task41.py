def mostFrequent(L):
    maxcount = 1
    element = L[0]
    for i in L:
        curcount = L.count(i)
        if curcount > maxcount:
            maxcount = curcount
            element = i
    return element


L = list(map(int, input().split()))
print(mostFrequent(L))
