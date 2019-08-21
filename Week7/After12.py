from sys import stdin
electionUSA = dict()
for line in stdin:
    curState = line.split()
    if curState[0] not in electionUSA:
        electionUSA[curState[0]] = 0
    electionUSA[curState[0]] += int(curState[1])
for candidate in sorted(electionUSA):
    print(candidate, electionUSA[candidate])
