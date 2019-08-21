def howManyUsers(s, n):
    userData = []
    fullData = 0
    for i in range(n):
        userData.append(int(input()))
        fullData += userData[i]
    userData.sort()
    if fullData <= s:
        return n
    count = 0
    i = 0
    while s - userData[i] >= 0:
        count += 1
        s -= userData[i]
        i += 1
    return count


L = list(map(int, input().split()))
print(howManyUsers(L[0], L[1]))
