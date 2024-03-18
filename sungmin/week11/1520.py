M, N = map(int, input().split())
DIR = [(1,0),(0,1),(-1,0),(0,-1)]
IS_IN = lambda y, x: 0 <= y < M and 0 <= x < N

graph = [list(map(int, input().split())) for _ in range(M)]
arrive = [[-1] * N for _ in range(M)]

def dp(y, x):
    if not IS_IN(y, x): return 0
    if y == M - 1 and x == N - 1: return 1
    
    if arrive[y][x] >= 0: return arrive[y][x]
    
    arrive[y][x] = 0
    for dy, dx in DIR:
        ny, nx = y + dy, x + dx
        if not IS_IN(ny, nx): continue
        if graph[y][x] > graph[ny][nx]:
            arrive[y][x] += dp(ny, nx)
    return arrive[y][x]

print(dp(0,0))