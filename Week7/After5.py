from sys import stdin
n = int(stdin.readline())
fullLanguages = set()       # Хотя бы один
allLanguages = set()        # Все
for pupil in range(1, n + 1):
    mi = int(stdin.readline())
    curLanguages = set()
    for i in range(mi):
        curLanguage = stdin.readline()
        fullLanguages.add(curLanguage)
        curLanguages.add(curLanguage)
    if pupil == 1:
        allLanguages |= curLanguages
    else:
        allLanguages &= curLanguages
print(len(allLanguages))
strAllLanguages = ''.join(allLanguages)
print(strAllLanguages.strip())
print(len(fullLanguages))
strFullLanguages = ''.join(fullLanguages)
print(strFullLanguages.strip())
