from math import ceil


def lag(n, p):
    if n == 1:
        if p > 0:
            print(1, end=' ')
        return 1
    elif not n:
        return 0
    i = int(n ** (1 / 3))
    while i >= ceil((n / 7) ** (1 / 3)):
        count = lag(n - i ** 3, p - 1)
        if count <= p - 1:
            print(i ** 3, end=' ')
        if p != 7 or count < 7:
            return count + 1
        i -= 1
    print(0)


n = int(input())
lag(n, 7)
