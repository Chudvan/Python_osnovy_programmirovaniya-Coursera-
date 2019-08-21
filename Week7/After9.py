from sys import stdin
n = int(stdin.readline())
cityCountryDict = dict()
for i in range(n):
    line = stdin.readline()
    lineList = line.split()
    for j in range(1, len(lineList)):
        city = lineList[j]
        cityCountryDict[city] = lineList[0]
amountCities = int(stdin.readline())
countryList = []
for i in range(amountCities):
    line = stdin.readline()
    line = line.strip()
    countryList.append(cityCountryDict[line])
print('\n'.join(countryList))
