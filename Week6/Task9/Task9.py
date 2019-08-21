def CountSort(L):
    listCount = [0] * 101
    for number in L:
        listCount[number] += 1
    LSort = []
    for number in range(101):
        for count in range(listCount[number]):
            LSort.append(number)
    return LSort


L = list(map(int, input().split()))
print(*CountSort(L))
