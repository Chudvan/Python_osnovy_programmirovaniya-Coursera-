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


def isPalindrome(x):
    if not x % 10:
        return False
    n = numberOfDigits(x)
    y = 0       # Будущее обратное число
    z = x       # Вспомогательная копия x
    for i in range(n):
        y *= 10
        y += z % 10
        z //= 10
    if x == y:
        return True
    return False


def allPalindromes(a, b):
    for i in range(a, b + 1):
        if isPalindrome(i):
            print(i)


a = int(input())
b = int(input())
allPalindromes(a, b)
