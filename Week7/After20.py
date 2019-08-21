def sonHeight(curRoot, dict_1, dict_2, curHeight):
    if curRoot not in dict_1:
        return
    for son in dict_1[curRoot]:
        dict_2[son] = curHeight + 1
        sonHeight(son, dict_1, dict_2, curHeight + 1)


n = int(input())
generation_1 = dict()       # Словарь отцов
allPeople = set()
allSons = set()
for i in range(n - 1):
    line = input()
    lineList = line.split()
    curParent = lineList[1]
    curSon = lineList[0]
    allPeople.add(curParent)
    allPeople.add(curSon)
    allSons.add(curSon)
    if curParent not in generation_1:
        generation_1[curParent] = set()
    generation_1[curParent].add(curSon)
root = (allPeople - allSons).pop()
generation_2 = dict()       # Словарь для задачи
generation_2[root] = 0
sonHeight(root, generation_1, generation_2, generation_2[root])
for son in sorted(generation_2):
    print(son, generation_2[son])
