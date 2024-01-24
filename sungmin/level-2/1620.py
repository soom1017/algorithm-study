import sys
input = sys.stdin.readline

N, M = map(int, input().split())
PM = [input()[:-1] for _ in range(N)]
PM_LOWER = [P.lower() for P in PM]

for _ in range(M):
    try:
        s = input()[:-1]
        print(PM[int(s) - 1])
    except ValueError:
        print(PM_LOWER.index(str(s).lower()) + 1)