def whichMore(inFile):
    amount = [0] * 99
    for line in inFile:
        cur = line.split()
        amount[int(cur[2]) - 1] += 1
    maxAmount = amount[0]
    for number in range(1, 99):
        if amount[number] > maxAmount:
            maxAmount = amount[number]
    for number in range(99):
        if amount[number] == maxAmount:
            print(number + 1, end=' ')


inFile = open('input.txt', 'r', encoding='utf-8')
whichMore(inFile)
