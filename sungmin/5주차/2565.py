import sys, bisect
input = sys.stdin.readline

N = int(input())
LINES = [list(map(int, input().split())) for _ in range(N)]
LINES.sort(key=lambda x:x[0])
LINES = [i[1] for i in LINES]

DP = [0]
for n in LINES:
    if n > DP[-1]:
        DP.append(n)
    else:
        idx = bisect.bisect_left(DP,n)
        DP[idx] = n

print(N - len(DP[1:]))
