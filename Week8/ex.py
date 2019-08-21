import os


for i in range(100, 111):
    os.system('move Lesson{}.py Task{}.py'.format(i, i - 99))
