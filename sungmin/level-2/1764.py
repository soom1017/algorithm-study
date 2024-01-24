import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
L = [input()[:-1] for _ in range(N)]
L.extend([input()[:-1] for _ in range(M)])
L.sort()

LS = deque()
LS.extend(L)

b = LS.popleft()
for _ in range(N + M - 1):
    c = LS.popleft()
    if b == c:
        LS.append(c)
    b = c

print(len(LS))
for i in LS: print(i)