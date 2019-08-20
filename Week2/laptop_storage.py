a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
n = 0

if a >= b and a >= c:   # a <= b <= c
    (c, a) = (a, c)
    if a > b:
        (b, a) = (a, b)
elif b >= a and b >= c:
    (c, b) = (b, c)
    if a > b:
        (b, a) = (a, b)
elif a > b:
    (b, a) = (a, b)

if d >= e and d >= f:   # d <= e <= f
    (f, d) = (d, f)
    if d > e:
        (e, d) = (d, e)
elif e >= d and e >= f:
    (f, e) = (e, f)
    if d > e:
        (e, d) = (d, e)
elif d > e:
    (e, d) = (d, e)

if c >= f and b >= e and a >= d:
    if n < (c // f) * (b // e) * (a // d):
        n = (c // f) * (b // e) * (a // d)
    if n < (c // e) * (b // f) * (a // d):
        n = (c // e) * (b // f) * (a // d)
    if n < (c // f) * (b // d) * (a // e):
        n = (c // f) * (b // d) * (a // e)
    if n < (c // d) * (b // f) * (a // e):
        n = (c // d) * (b // f) * (a // e)
    if n < (c // e) * (b // d) * (a // f):
        n = (c // e) * (b // d) * (a // f)
    if n < (c // d) * (b // e) * (a // f):
        n = (c // d) * (b // e) * (a // f)
print(n)
