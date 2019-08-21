inFile = open('input.txt', 'r', encoding='utf-8')
dataBase = dict()
for line in inFile:
    curLine = line.split()
    operation = curLine[0]
    if operation == 'INCOME':
        p = int(curLine[1])
        for client in dataBase:
            if dataBase[client] > 0:
                dataBase[client] += int(dataBase[client] * p / 100)
    else:
        client = curLine[1]
        if operation == 'BALANCE':
            if client not in dataBase:
                print('ERROR')
            else:
                print(dataBase[client])
        else:
            if client not in dataBase:
                dataBase[client] = 0
            if operation == 'TRANSFER':
                client2 = curLine[2]
                amount = int(curLine[3])
                if client2 not in dataBase:
                    dataBase[client2] = 0
                dataBase[client] -= amount
                dataBase[client2] += amount
            else:
                amount = int(curLine[2])
                if operation == 'DEPOSIT':
                    dataBase[client] += amount
                elif operation == 'WITHDRAW':
                    dataBase[client] -= amount
