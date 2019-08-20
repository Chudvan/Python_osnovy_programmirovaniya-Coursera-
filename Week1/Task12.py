a = int(input())
b = int(input())
n = int(input())

price = a * 100 + b
cost = price * n
print(cost // 100, cost % 100)
