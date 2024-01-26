# 백조의 호수: https://acmicpc.net/problem/3197
from collections import deque

r, c = map(int, input().split())
in_graph = lambda x, y: 0 <= x < r and 0 <= y < c

# 초기 그래프, 백조 위치 저장
data = [list(input()) for _ in range(r)]
swan_idx = []
for i in range(r):
    for j in range(c):
        if data[i][j] == 'L':
            swan_idx.append((i, j))
            data[i][j] = '.'
            if len(swan_idx) == 2:
                break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# union-find 로직
parents = [[(i, j) for j in range(c)] for i in range(r)]

def find(parents, v):
    x, y = v
    if parents[x][y] == v:
        return v
    parents[x][y] = find(parents, parents[x][y])
    return parents[x][y]

def union(parents, v1, v2):
    parent1 = find(parents, v1)
    parent2 = find(parents, v2)
    if parent1 > parent2:
        parents[parent2[0]][parent2[1]] = parent1
    else:
        parents[parent1[0]][parent1[1]] = parent2
        
# 물 공간 집합 탐색
to_water = deque()

for i in range(r):
    for j in range(c):
        if data[i][j] != '.':
            continue
        # 물 공간이라면 옆의 물 공간과 union ('O'로 방문 표시)
        data[i][j] = 'O'
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if in_graph(nx, ny):
                if data[nx][ny] == '.':
                    union(parents, (i, j), (nx, ny))
                elif data[nx][ny] == 'X':
                    to_water.append((nx, ny))
                        
day = 0
while find(parents, swan_idx[0]) != find(parents, swan_idx[1]):
    day += 1
    to_water_tmp = deque()
    while to_water:
        # 녹는 지점으로부터 4방향 탐색하여 다음날 녹을 지점 저장
        x, y = to_water.popleft()
        if data[x][y] == 'O':
            continue
        # 녹은 뒤 방문한 것까지 적용
        data[x][y] = 'O'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if in_graph(nx, ny):
                if data[nx][ny] == 'X':
                    to_water_tmp.append((nx, ny))
                else:
                    # 이미 녹아있는 지점과 union
                    union(parents, (x, y), (nx, ny))
    to_water = to_water_tmp

print(day)