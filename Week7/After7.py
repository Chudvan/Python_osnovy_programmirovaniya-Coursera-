n, k = tuple(map(int, input(). split()))
allStrikes = set()
for party in range(k):
    a, b = tuple(map(int, input(). split()))
    allStrikes |= set(range(a, n + 1, b))
allWeekends = set(range(6, n + 1, 7)) | set(range(7, n + 1, 7))
print(len(allStrikes - allWeekends))
