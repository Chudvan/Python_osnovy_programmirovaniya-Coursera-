a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * d - b * c
if det:
    x = (e * d - f * b) / det
    y = (a * f - e * c) / det
    print(2, x, y)
else:
    if a == b == c == d == 0:
        if e == f == 0:
            print(5)
        else:
            print(0)
    else:
        if b:
            if e * d == b * f:
                if a:
                    print(1, - a / b, e / b)
                else:
                    print(4, e / b)
            else:
                print(0)
        else:
            if d:
                if e:
                    print(0)
                else:
                    if c:
                        print(1, - c / d, f / d)
                    else:
                        print(4, f / d)
            else:
                if a:
                    if a * f == e * c:
                        print(3, e / a)
                    else:
                        print(0)
                else:
                    if e:
                        print(0)
                    else:
                        print(3, f / c)
