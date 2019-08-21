def Intersection(A, B):
    lenA = len(A)
    lenB = len(B)
    C = []
    i = 0
    j = 0
    while i < lenA and j < lenB:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            C.append(A[i])
            i += 1
            j += 1
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*Intersection(A, B))
