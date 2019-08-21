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
        votes[i] = (allVotes.count(parties[i]), parties[i])
        numVotes += votes[i][0]
    votes.sort(key=lambda cur: (-cur[0], cur[1]))
    for i in range(numParties):
        print(votes[i][1], end='')


inFile = open('input.txt', 'r', encoding='utf-8')
whoWins(inFile)
