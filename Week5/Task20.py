def howManyMore(L):
    length = len(L)
    if length < 3:
        return 0
    last = L[0]
    count = 0
    for i in range(1, length - 1):
        if L[i] > last and L[i] > L[i + 1]:
            count += 1
        last = L[i]
    return count


L = list(map(int, input().split()))
print(howManyMore(L))
