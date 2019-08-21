from math import ceil, sqrt
print(
    2,
    *filter(
        lambda x:
            not any(map(lambda y: x % y == 0, range(2, ceil(sqrt(x)) + 1))),
        range(3, int(input()) + 1)
    )
)
