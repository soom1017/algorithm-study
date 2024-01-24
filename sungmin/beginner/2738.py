N, _ = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j] + B[i][j], end=" ")
    print()