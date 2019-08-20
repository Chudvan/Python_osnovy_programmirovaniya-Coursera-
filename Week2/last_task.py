n = int(input())
last = 0
countD = 0
countI = 0
maxCount = 0
lastMax = 0
currentMax = 0
minDistance = 0
i = -1
while n:
    i += 1
    if last < n and last != 0:
        if countD:
            if maxCount < countD:
                maxCount = countD
            countD = 0
            countI = 1
        last = n
        countI += 1
    elif last > n:
        if countI:
            if maxCount < countI:
                maxCount = countI
            countI = 0
            countD = 1
            lastMax = currentMax
            currentMax = i-1
            if lastMax != 0:
                if currentMax - lastMax < minDistance or minDistance == 0:
                    minDistance = currentMax - lastMax
        last = n
        countD += 1
    else:
        if maxCount < countI:
            maxCount = countI
        elif maxCount < countD:
            maxCount = countD
        last = n
        countI = 1
        countD = 1
    n = int(input())
if maxCount < countI:
    maxCount = countI
elif maxCount < countD:
    maxCount = countD
print(minDistance)
