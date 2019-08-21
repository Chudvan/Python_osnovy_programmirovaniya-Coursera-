from sys import stdin


class Party:
    numberParty = 0
    residue = 0
    numberVotes = 0
    numberDeputies = 0


partyDict = dict()
allVotes = 0
number = 1
for line in stdin:
    curParty = Party()
    curParty.numberParty = number
    curParty.numberVotes = int(line.split()[-1])
    nameParty = ' '.join(line.split()[:-1])
    partyDict[nameParty] = curParty
    allVotes += curParty.numberVotes
    number += 1
coefficient = allVotes / 450
aPlaces = 450
for curParty in partyDict:
    cur = partyDict[curParty]       # Классный ход, создать ссылку на эл-т мас
    cur.numberDeputies = int(cur.numberVotes / coefficient)
    cur.residue = cur.numberVotes % coefficient
    aPlaces -= cur.numberDeputies


def residueSort(key):
    return partyDict[key].residue       # Плохо, ГЛОБАЛЬНОЕ обращение


while aPlaces:
    for curParty in sorted(partyDict, key=residueSort, reverse=True):
        partyDict[curParty].numberDeputies += 1
        aPlaces -= 1
        if not aPlaces:
            break
for curParty in sorted(partyDict, key=lambda p: partyDict[p].numberParty):
    print(curParty, partyDict[curParty].numberDeputies)
