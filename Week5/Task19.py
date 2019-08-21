def sign(x):
    if x >= 0:
        return 1
    return -1


def neighbours(L):
    cursign = sign(L[0])
    i = 1
    length = len(L)
    while i < length:
        nextsign = sign(L[i])
        if nextsign == cursign:
            print(L[i - 1], L[i])
            return
        cursign = nextsign
        i += 1


L = list(map(int, input().split()))
neighbours(L)
