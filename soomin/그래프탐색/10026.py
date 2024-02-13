# 적록색약: https://www.acmicpc.net/problem/10026
from collections import deque

n = int(input())
data = [list(input()) for _ in range(n)]
visited = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, blind=False):
    queue = deque([(x, y)])
    color = data[y][x]
    if blind and color in ['R', 'G']:
        color = ['R', 'G']
    visited[y][x] = True
    
    while queue:
        v = queue.popleft()

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[ny][nx] in color and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
    return 1

# count, visited 초기화
count = 0
for i in range(n):
    visited.append([False] * n)
# 색약이 아닌 사람
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            count += bfs(x, y)

# blind_count, visited 초기화
blind_count = 0
for i in range(n):
    for j in range(n):
        visited[i][j] = False
# 색약인 사람
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            blind_count += bfs(x, y, blind=True)

print(count, blind_count)