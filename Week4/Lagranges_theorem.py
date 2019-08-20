from math import sqrt, ceil


def lag(n, p):
    if n == 1:
        if p > 0:
            print(1, end=' ')
        return 1
    elif not n:
        return 0
    i = int(sqrt(n))
    while i >= ceil(sqrt(n / 4)):
        count = lag(n - i ** 2, p - 1)
        if count <= p - 1:
            print(i, end=' ')
        if p != 4 or count < 4:
            return count + 1
        i -= 1


n = int(input())
lag(n, 4)
