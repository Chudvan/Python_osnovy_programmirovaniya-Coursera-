def isEven(n):
    if n % 2:
        return False
    return True


def decreaserange(n):
    first = 10 ** n - 1
    last = 10 ** (n - 1)
    for i in range(first, last - 1, - 1):
        if not isEven(i):
            print(i, end=' ')


n = int(input())
decreaserange(n)
