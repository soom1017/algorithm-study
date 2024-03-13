N = int(input())

ARR = [[0] * 10 for _ in range(N)]
for i in range(1, len(ARR[0])):
    ARR[0][i] = 1


for i in range(N):
    for j in range(10):
        if i-1 >= 0:
            if j-1 >= 0: ARR[i][j] += ARR[i-1][j-1] % 1000000000
            if j+1 < 10: ARR[i][j] += ARR[i-1][j+1] % 1000000000

print(sum(ARR[N-1]) % 1000000000)