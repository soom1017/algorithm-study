T = int(input())
for _ in range(T):
    N = int(input())
    applicants = []

    for sc in range(N):
        applicants.append(list(map(int, input().split())))
    
    applicants.sort()
    second_score = applicants[0][1]

    cnt = 1

    for i in range(1, N):
        if applicants[i][1] < second_score:
            cnt += 1
            second_score = applicants[i][1]
    
    print(cnt)