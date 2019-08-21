def minMark(inFile, outFile):
    k = int(inFile.readline())

    class Entrant:
        Exam1 = 0
        Exam2 = 0
        Exam3 = 0
        Sum = 0

    entrants = []
    for line in inFile:
        cur = line.split()
        entrant = Entrant()
        i = 0
        while cur[i].isalpha():
            i += 1
        if int(cur[i]) < 40 or int(cur[i + 1]) < 40 or int(cur[i + 2]) < 40:
            continue
        entrant.Exam1 = int(cur[i])
        entrant.Exam2 = int(cur[i + 1])
        entrant.Exam3 = int(cur[i + 2])
        entrants.append(entrant)
    if len(entrants) <= k:
        print(0, file=outFile)
        return
    for entrant in entrants:
        entrant.Sum = entrant.Exam1 + entrant.Exam2 + entrant.Exam3
    entrants.sort(key=lambda ent: ent.Sum, reverse=True)
    curCount = 1
    for i in range(1, k + 1):
        if entrants[i].Sum == entrants[i - 1].Sum:
            curCount += 1
            if curCount > k:
                print(1, file=outFile)
                return
        else:
            lastSum = entrants[i - curCount].Sum
            curCount = 1
    print(lastSum, file=outFile)


inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
minMark(inFile, outFile)
