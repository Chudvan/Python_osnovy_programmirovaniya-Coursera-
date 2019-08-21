from sys import stdin
n = int(stdin.readline())
synonimDict = dict()
for i in range(n):
    line = stdin.readline()
    lineList = line.split()
    synonimDict[lineList[0]] = lineList[1]
    synonimDict[lineList[1]] = lineList[0]
word = input()
print(synonimDict[word])
