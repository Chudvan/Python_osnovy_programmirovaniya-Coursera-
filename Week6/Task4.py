def howManyPairs(L, size):
    count = 0
    lastSize = 0
    L.sort()
    for curSize in L:
        if curSize >= size:
            if not count:
                count += 1
                lastSize = curSize
            elif curSize - lastSize >= 3:
                count += 1
                lastSize = curSize
    return count


size = int(input())
L = list(map(int, input().split()))
print(howManyPairs(L, size))
