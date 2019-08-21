def secondMax():
    L = list(map(int, input().split()))
    maxi = L[0]
    curindex = 0
    for i in range(1, len(L)):
        if L[i] >= maxi:
            curindex = i
            maxi = L[i]
    return maxi, curindex


print(*secondMax())
