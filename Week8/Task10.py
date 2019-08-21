from functools import reduce
print(
    *map(
        lambda x: reduce(
            lambda a, b: int((not a or not b) and (bool(a) or bool(b))),
            x
        ),
        zip(*map(
            lambda x: tuple(map(int, input().split())),
            range(int(input()))
            )
        )
    )
)
