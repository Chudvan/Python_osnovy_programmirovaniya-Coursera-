L = list(map(int, input().split()))
L = [i for i in L if i % 2 == 0]
print(*L)
