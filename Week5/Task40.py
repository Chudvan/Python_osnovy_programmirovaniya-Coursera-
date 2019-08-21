def listCompression(L):
    indexNul = -1   # Инициализируем переменную, для первой проверки условия
    for i in range(len(L)):
        if indexNul == -1 and not L[i]:
            indexNul = i
        if L[i] and indexNul < i and indexNul != -1:
            (L[i], L[indexNul]) = (L[indexNul], L[i])
            indexNul += 1   # После swap'a next индекс нуля на единицу больше


L = list(map(int, input().split()))
listCompression(L)
print(*L)
