from collections import deque

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DIR = [(0,1),(1,0),(0,-1),(-1,0)]

in_map = lambda ny, nx : 0 <= ny < N and 0 <= nx < M

def air_side(y, x):
    ret = 0
    for dy, dx in DIR:
        ny = y + dy
        nx = x + dx
        if MAP[ny][nx] == 2: ret += 1
    return ret

def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    melt = list()
    
    MAP[0][0] = 2
    q.append((0,0))
    while q:
        y, x = q.popleft()
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if not in_map(ny, nx) or visited[ny][nx]: continue
            visited[ny][nx] = 1
            
            if MAP[ny][nx] == 0 or MAP[ny][nx] == 2:
                MAP[ny][nx] = 2
                q.append((ny, nx))
            elif MAP[ny][nx] == 1:
                melt.append((ny, nx))
    
    not_melt = 0
    for y, x in melt:
        if air_side(y, x) >= 2: MAP[y][x] = 0
        else: not_melt += 1
    return len(melt) - not_melt

elapsed = 0
sum_cheeze = 0
for row in MAP: sum_cheeze += sum(row)

while True:
    elapsed += 1
    melt_cheeze = bfs()
    sum_cheeze -= melt_cheeze
    if not sum_cheeze: break

print(elapsed)