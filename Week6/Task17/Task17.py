def tripCost(distanceList, costList):
    distanceList.sort()
    costList.sort(reverse=True)
    n = len(distanceList)
    cost = 0
    for worker in range(n):
        cost += distanceList[worker] * costList[worker]
    return cost


distanceList = list(map(int, input().split()))
costList = list(map(int, input().split()))
print(tripCost(distanceList, costList))
