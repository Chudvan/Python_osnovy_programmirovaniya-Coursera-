def howMany(L):
    length = len(L)
    if not length:
        return 0
    count = 1
    for i in range(1, length):
        if L[i] != L[i - 1]:
            count += 1
    return count


L = list(map(int, input().split()))
print(howMany(L))
