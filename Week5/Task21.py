def maxNum(L):
    maxi = L[0]
    index = 0
    for i in range(1, len(L)):
        if L[i] > maxi:
            maxi = L[i]
            index = i
    return maxi, index


L = list(map(int, input().split()))
print(*maxNum(L))
