print(
    *map(
        lambda x, y: int((not x or not y) and (bool(x) or bool(y))),
        map(int, input().split()),
        map(int, input().split())
    )
)
