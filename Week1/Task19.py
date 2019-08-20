h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

time_1 = h1 * 3600 + m1 * 60 + s1
time_2 = h2 * 3600 + m2 * 60 + s2
difference = time_2 - time_1

print(difference)
