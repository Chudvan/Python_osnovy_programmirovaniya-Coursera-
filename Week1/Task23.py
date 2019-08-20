a = int(input())
b = int(input())
c = a + 2
d = b + 2
print(((c // d) * a + (d // c) * b) // ((c // d) + (d // c)))
