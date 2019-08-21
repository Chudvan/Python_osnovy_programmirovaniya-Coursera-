def number(n):
    count = 0
    for i in range(n):
        x = int(input())
        if not x:
            count += 1
    return count


n = int(input())
print(number(n))
