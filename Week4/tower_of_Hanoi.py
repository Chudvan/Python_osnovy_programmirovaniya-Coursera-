def max2(x, y):
    if x > y:
        return y, x
    return x, y


def another(x, y):
    mini, maxi = max2(x, y)
    if mini == 1:
        if maxi == 2:
            return 3
        return 2
    return 1


def move(n, x, y):
    z = another(x, y)
    if n > 1:
        move(n - 1, x, z)
        print(n, x, y)
        move(n - 1, z, y)
    elif n == 1:
        print(1, x, y)


n = int(input())
move(n, 1, 3)
