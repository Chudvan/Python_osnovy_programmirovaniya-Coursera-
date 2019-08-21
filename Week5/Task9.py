def DiafantovoEquation(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def numberOfSolutions(a, b, c, d, e):
    count = 0
    for i in range(1001):
        if i != e and not DiafantovoEquation(a, b, c, d, i):
            count += 1
    return count


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(numberOfSolutions(a, b, c, d, e))
