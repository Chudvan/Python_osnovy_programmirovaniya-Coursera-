def cubes(inFile):
    n, m = map(int, inFile.readline().split())
    i = 1
    ann = set()
    boris = set()
    for line in inFile:
        color = int(line)
        if i <= n:
            ann.add(color)
        else:
            boris.add(color)
        i += 1
    intersection = ann & boris
    otherAnn = ann - intersection
    otherBoris = boris - intersection
    print(len(intersection))
    print(*sorted(intersection))
    print(len(otherAnn))
    print(*sorted(otherAnn))
    print(len(otherBoris))
    print(*sorted(otherBoris))


inFile = open('input.txt', 'r', encoding='utf-8')
cubes(inFile)
