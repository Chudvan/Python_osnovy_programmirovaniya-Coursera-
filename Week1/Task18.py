n = int(input())

hours = (n // 3600) % 24
min_ = (n % 3600) // 60
minutes_1 = min_ // 10
minutes_2 = min_ % 10
sec = n % 60
seconds_1 = sec // 10
seconds_2 = sec % 10
print(hours, ':', minutes_1, minutes_2, ':', seconds_1, seconds_2, sep='')
