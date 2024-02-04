from collections import deque
import sys;input=sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
mp = [0] + ['0' + input() for _ in range(N)]
dist = [[0]*(M+1) for _ in range(N+1)]

q = deque([[1,1]])
dist[1][1] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 1 <= nx <= M and 1 <= ny <= N and mp[ny][nx] == '1' and dist[ny][nx] == 0:
            dist[ny][nx] = dist[y][x] + 1
            q.append([nx, ny])

print(dist[N][M])

# BFS