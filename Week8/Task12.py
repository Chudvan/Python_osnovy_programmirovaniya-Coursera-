from itertools import permutations
list(map(lambda g:
        print(*(list(
            map(
                lambda h: tuple(map(lambda j: j[1], h)),
                map(
                    lambda p: sorted(p, key=lambda s: s[0]),
                    filter(
                        lambda c: all(
                            map(
                                lambda t: (not t[0] or not t[1]) and (bool(t[0]) or bool(t[1])),
                                map(
                                    lambda a: (c[a[0] - 1] < c[a[1] - 1], c[a[2] - 1] < c[a[3] - 1]),
                                    tuple(map(lambda x: tuple(map(int, input().split())), range(g[1])))
                                )
                            )
                        ),
                        tuple(map(
                                lambda y: sorted(enumerate(y), key=lambda z: z[1]),
                                permutations(range(1, g[0] + 1))
                                ))
                    )
                )
            )
        ) + [(0, )])[0]),
         [tuple(map(int, input().split()))]))
