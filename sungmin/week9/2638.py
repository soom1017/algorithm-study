from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DIR = [(0,1),(1,0),(0,-1),(-1,0)]

in_map = lambda ny, nx : 0 <= ny < N and 0 <= nx < M

def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    melt = list()
    
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if visited[ny][nx] or not in_map(ny, nx): continue
            visited[ny][nx] = 1
            
            if MAP[ny][nx] == 0: q.append((ny, nx))
            elif MAP[ny][nx] == 1: melt.append((ny, nx))
    for y, x in melt: MAP[y][x] = 0

    return len(melt)

elapsed = 0
sum_cheeze = 0
for row in MAP: sum_cheeze += sum(row)

while True:
    elapsed += 1
    melt_cheeze = bfs()
    sum_cheeze -= melt_cheeze
    if not sum_cheeze: break

print(elapsed)