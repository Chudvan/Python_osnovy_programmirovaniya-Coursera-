from math import log, ceil


def isTensDegree(x):
    while not x % 10:
        x //= 10
    if x == 1:
        return True
    return False


def numberOfDigits(x):
    if isTensDegree(x):
        return ceil(log(x, 10) + 1)
    return ceil(log(x, 10))


def multiplicationDigits(x):
    n = numberOfDigits(x)
    count = 1
    for i in range(n - 1):
        count *= x % 10
        x //= 10
    count *= x
    return count


def wonderfulNumbers(n):
    first = 10 ** (n - 1)
    last = 10 ** n
    L = ()
    for i in range(first, last):
        if i == 2 * multiplicationDigits(i):
            L += ('%d' % i, )
    print(' '.join(L))


wonderfulNumbers(2)
