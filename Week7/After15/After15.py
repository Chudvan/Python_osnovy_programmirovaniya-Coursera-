def russianElection(inFile, outFile):
    votes = dict()
    allVotes = 0
    for line in inFile:
        allVotes += 1
        curCandidate = line.strip()
        if curCandidate not in votes:
            votes[curCandidate] = 0
        votes[curCandidate] += 1
    if len(votes) == 1:
        print(curCandidate, file=outFile)
        return
    allCandidates = tuple(votes.items())
    maxVotes = allCandidates[0][1]
    mrPresident = allCandidates[0][0]
    lastMax = allCandidates[1][1]
    vicePresident = allCandidates[1][0]
    for candidate in votes:
        if votes[candidate] > maxVotes:
            lastMax = maxVotes
            maxVotes = votes[candidate]
            vicePresident = mrPresident
            mrPresident = candidate
        elif votes[candidate] > lastMax and candidate != mrPresident:
            lastMax = votes[candidate]
            vicePresident = candidate
    if 2 * maxVotes > allVotes:
        print(mrPresident, file=outFile)
    else:
        print(mrPresident, '\n', vicePresident, file=outFile, sep='')


inFile = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
russianElection(inFile, outFile)
