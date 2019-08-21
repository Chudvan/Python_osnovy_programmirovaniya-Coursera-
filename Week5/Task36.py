def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


def C(n, k):
    return factorial(k) // (factorial(n) * factorial(k - n))


def howManyPairs(L):
    count = 0
    secondlist = []
    for i in L:
        nduplicate = L.count(i)
        if nduplicate >= 2 and i not in secondlist:
            count += C(2, nduplicate)
            secondlist.append(i)
    return count


L = list(map(int, input().split()))
print(howManyPairs(L))
