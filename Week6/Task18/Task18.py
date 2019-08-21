def whoWins(inFile):
    parties = []
    inFile.readline()
    line = inFile.readline()
    while line != 'VOTES:\n':
        parties.append(line)
        line = inFile.readline()
    numParties = len(parties)
    votes = [0] * numParties
    allVotes = inFile.read()
    numVotes = 0
    for i in range(numParties):
        votes[i] = allVotes.count(parties[i])
        numVotes += votes[i]
    for i in range(numParties):
        if 100 * votes[i] >= 7 * numVotes:
            print(parties[i], end='')


inFile = open('input.txt', 'r', encoding='utf-8')
whoWins(inFile)
