def max2(a, b):
    if a > b:
        return b, a
    return a, b


def gcd(a, b):
    mini, maxi = max2(a, b)
    if maxi % mini:
        return gcd(maxi % mini, mini)
    return mini


def ReduceFraction(n, m):
    nod = gcd(n, m)
    return n // nod, m // nod


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
