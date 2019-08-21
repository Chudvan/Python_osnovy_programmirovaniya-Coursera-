def stairs(n):
    t = ()
    for i in range(1, n + 1):
        t += (str(i), )
        print(''.join(t))


n = int(input())
stairs(n)
