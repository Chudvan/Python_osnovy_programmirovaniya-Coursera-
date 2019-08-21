def isKeyCrash(n, numberClicks, allClicks):
    countClicks = [0] * n
    for key in allClicks:
        countClicks[key - 1] += 1
    for i in range(n):
        if countClicks[i] <= numberClicks[i]:
            print('NO')
        else:
            print('YES')


n = int(input())
numberClicks = list(map(int, input().split()))
k = int(input())
allClicks = list(map(int, input().split()))
isKeyCrash(n, numberClicks, allClicks)
