def participantsSort(n):
    participants = []
    for i in range(n):
        participant = tuple(map(str, input().split()))
        participants.append(participant)
    participants.sort(key=lambda cur: int(cur[1]), reverse=True)
    for participant in participants:
        print(participant[0])


n = int(input())
participantsSort(n)
