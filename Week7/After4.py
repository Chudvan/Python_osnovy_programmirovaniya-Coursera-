from sys import stdin
n = int(stdin.readline())
possibleSet = set(range(1, n + 1))
line = stdin.readline()
answer = ''
while line != 'HELP\n':
    curSet = set(map(int, line.split()))
    if 2 * len(possibleSet & curSet) <= len(possibleSet):
        answer += 'NO\n'
        possibleSet -= curSet
    else:
        answer += 'YES\n'
        possibleSet &= curSet
    line = stdin.readline()
print(answer, end='')
print(*sorted(possibleSet))
