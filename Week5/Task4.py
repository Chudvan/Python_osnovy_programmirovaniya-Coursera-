def amount(n):
    count = 0
    for i in range(1, n + 1):
        count += i ** 2
    return count


n = int(input())
print(amount(n))
