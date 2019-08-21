def amountOfFactorials(n):
    if n == 1:
        return 1
    count = n
    for i in range(n - 1, 1, -1):
        count = i * (1 + count)
    return 1 + count


n = int(input())
print(amountOfFactorials(n))
