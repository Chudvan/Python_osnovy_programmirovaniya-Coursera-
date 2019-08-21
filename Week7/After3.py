from sys import stdin
n = int(stdin.readline())
possibleSet = set(range(1, n + 1))
for line in stdin:
    if line == 'YES\n':
        possibleSet &= curSet
    elif line == 'NO\n':
        possibleSet -= curSet
    elif line != 'HELP\n':
        curSet = set(map(int, line.split()))
print(*sorted(possibleSet))
