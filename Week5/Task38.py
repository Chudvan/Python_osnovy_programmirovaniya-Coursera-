def skittle(n, k):
    skittles = ['I'] * n
    for i in range(k):
        left, right = map(int, input().split())
        for j in range(n):
            if j >= left - 1 and j <= right - 1:
                skittles[j] = '.'
    print(''.join(skittles))


n, k = map(int, input().split())
skittle(n, k)
