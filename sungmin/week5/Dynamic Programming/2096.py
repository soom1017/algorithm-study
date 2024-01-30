import sys
input = sys.stdin.readline

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

DP = [MAP[0][0],MAP[0][1],MAP[0][2]]
# MAX
for i in range(1, N):
    DP = [
        MAP[i][0] + max(DP[:2]),
        MAP[i][1] + max(DP[:]),
        MAP[i][2] + max(DP[1:]),
    ]
nmax = max(DP)

DP = [MAP[0][0],MAP[0][1],MAP[0][2]]
# MAX
for i in range(1, N):
    DP = [
        MAP[i][0] + min(DP[:2]),
        MAP[i][1] + min(DP[:]),
        MAP[i][2] + min(DP[1:]),
    ]
nmin = min(DP)

print(nmax, nmin)