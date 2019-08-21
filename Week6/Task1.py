def merge(A, B):
    lenA = len(A)
    lenB = len(B)
    C = []
    i = 0
    j = 0
    while i < lenA and j < lenB:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < lenA:
        C.append(A[i])
        i += 1
    while j < lenB:
        C.append(B[j])
        j += 1
    return C


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
