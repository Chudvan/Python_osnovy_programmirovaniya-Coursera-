def flags(n):
    print('+___ ' * n)
    for i in range(1, n + 1):
        print('|%d /' % i, end=' ')
    print('')
    print('|__\\ ' * n)
    print('|    ' * n)


n = int(input())
flags(n)
