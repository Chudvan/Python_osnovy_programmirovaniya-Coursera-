l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())

if l1 <= r2 and l2 <= r1:   # 1 ⋂ 2
    a = True
else:
    a = False

if l1 <= r3 and l3 <= r1:   # 1 ⋂ 3
    b = True
else:
    b = False

if l3 <= r2 and l2 <= r3:   # 2 ⋂ 3
    c = True
else:
    c = False

long1 = r1 - l1  # Длина 1
long2 = r2 - l2  # Длина 2
long3 = r3 - l3  # Длина 3

if a:   # Расстояние м/у 1 и 2
    distance12 = 0
elif l2 > r1:
    distance12 = l2 - r1
else:
    distance12 = l1 - r2

if b:   # Расстояние м/у 1 и 3
    distance13 = 0
elif l3 > r1:
    distance13 = l3 - r1
else:
    distance13 = l1 - r3

if c:   # Расстояние м/у 2 и 3
    distance23 = 0
elif l3 > r2:
    distance23 = l3 - r2
else:
    distance23 = l2 - r3

if not a and not b and not c:
    if long1 >= distance23:
        print(1)
    elif long2 >= distance13:
        print(2)
    elif long3 >= distance12:
        print(3)
    else:
        print(-1)

elif not a and not b and c:
    print(1)
elif not a and b and not c:
    if long1 >= distance23:
        print(1)
    else:
        print(2)
elif not a and b and c:
    print(0)
elif a and not b and not c:
    if long1 >= distance23:
        print(1)
    elif long2 >= distance13:
        print(2)
    else:
        print(3)
elif (a and not b and c) or (a and b and not c) or (a and b and c):
    print(0)
