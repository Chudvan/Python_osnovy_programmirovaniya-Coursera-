def max2(a, b):
    if a > b:
        return b, a
    return a, b


f1Bus, e1Bus, f2Bus, e2Bus = list(map(int, input().split()))
f1Bus, e1Bus = max2(f1Bus, e1Bus)
f2Bus, e2Bus = max2(f2Bus, e2Bus)
if f1Bus <= e2Bus and f2Bus <= e1Bus:
    # Исключаем случаи, когда множества ввобще не пересекаются.
    firstStops = set(range(f1Bus, e1Bus + 1))
    secondStops = set(range(f2Bus, e2Bus + 1))
    print(len(firstStops.intersection(secondStops)))
else:
    print(0)
