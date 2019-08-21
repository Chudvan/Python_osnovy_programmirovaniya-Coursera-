L = input().split()
str1 = ' ' + ' '.join(L)
count = str1.count(' 0') + str1.count('-')
print(len(L) - count)
