def petya(L, growth):
    i = 0
    length = len(L)
    while i < length and L[i] >= growth:
        i += 1
    return i + 1


L = list(map(int, input().split()))
growth = int(input())
print(petya(L, growth))
