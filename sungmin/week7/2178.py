import sys
from collections import deque

input = sys.stdin.readline

DIR = [(1,0),(0,1),(-1,0),(0,-1)]
N, M = map(int, input().rstrip().split())

is_in = lambda y, x : 0 <= y < N and 0 <= x < M

graph = list()
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
q = deque()
q.append((0, 0))

while q:
    y, x = q.popleft()

    for dy, dx in DIR:
        ny, nx = y + dy, x + dx

        if is_in(ny, nx) and graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))

print(graph[N-1][M-1])