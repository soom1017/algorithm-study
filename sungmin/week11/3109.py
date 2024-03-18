R, C = map(int, input().split())
IS_EMPTY = lambda x: 1 if x == '.' else 0
IS_IN = lambda y, x: 0 <= y < R and 0 <= x < C
DIR = [(-1,1),(0,1),(1,1)]

graph = [list(map(IS_EMPTY, list(input()))) for _ in range(R)]
visit = [[0] * C for _ in range(R)]

def dp(y, x, conn):
    if visit[y][x]: return 0
    visit[y][x] = 1
    if x == C - 1: return 1

    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if not IS_IN(ny, nx): continue
        if not graph[ny][nx]: continue
        if visit[ny][nx]: continue
        if dp(ny, nx, conn):
            return 1
    return 0

for y in range(R): dp(y, 0, y)

print(sum([visit[y][C - 1] for y in range(R)]))