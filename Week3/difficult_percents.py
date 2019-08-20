p = int(input())
x = int(input())
y = int(input())
k = int(input())
i = 1
money = x * 100 + y
percent = 100 + p
capital = money
while i <= k:
    capital *= percent
    capital //= 100
    i += 1
print(capital // 100, capital % 100)
