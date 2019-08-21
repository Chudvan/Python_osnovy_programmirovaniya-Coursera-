def defense(n, villages, m, shelters):
    villagesTuple = []
    sheltersTuple = []
    for i in range(n):
        villagesTuple.append((villages[i], i))
    for i in range(m):
        sheltersTuple.append((shelters[i], i + 1))
    villagesTuple.sort()
    sheltersTuple.sort()
    previousShelterIndex = 0
    curDistance = 1000000000
    listSalvation = [0] * n
    for village in villagesTuple:
        for i in range(previousShelterIndex, m):
            if abs(village[0] - sheltersTuple[i][0]) <= curDistance:
                curDistance = abs(village[0] - sheltersTuple[i][0])
                if i == m - 1:
                    listSalvation[village[1]] = sheltersTuple[i][1]
                    previousShelterIndex = i
                    curDistance = 1000000000
            else:
                listSalvation[village[1]] = sheltersTuple[i - 1][1]
                previousShelterIndex = i - 1
                curDistance = 1000000000
                break
    return listSalvation


n = int(input())
villages = list(map(int, input().split()))
m = int(input())
shelters = list(map(int, input().split()))
print(*defense(n, villages, m, shelters))
