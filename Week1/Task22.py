n = int(input())
a = (n // 1000) * 10 + (n // 100) % 10 + 2
b = (n % 10) * 10 + (n // 10) % 10 + 2

print(int(a == b))
