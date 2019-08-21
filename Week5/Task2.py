def max2(a, b):
    if a < b:
        return 1
    return -1


a = int(input())
b = int(input())
m = max2(a, b)
for i in range(a, b + m, m):
    print(i, end=' ')
