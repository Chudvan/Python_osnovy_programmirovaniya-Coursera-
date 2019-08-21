from sys import stdin
wordSet = set()
for line in stdin:
    curSet = set(line.split())
    wordSet |= curSet
print(len(wordSet))
