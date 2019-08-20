from math import sqrt


def squareoutput():
    n = int(input())
    if n:
        count = squareoutput()
        if n == (int(sqrt(n))) ** 2:
            print('', n, end='')
            count += 1
        return count
    return 0


if not squareoutput():
    print(0)
