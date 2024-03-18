N = int(input())
DIR = [(0,1),(1,0)]
IS_IN = lambda x: 0 <= x < N

graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
is_arrive = 0

q = list([(0,0)]) # y, x
while q:
    y, x = q.pop()
    if graph[y][x] == -1: 
        is_arrive = 1
        break

    if visit[y][x]: continue
    visit[y][x] = 1
    if graph[y][x] == 0: continue
    
    for dy, dx in DIR:
        ny, nx = y + dy * graph[y][x], x + dx * graph[y][x]
        if IS_IN(ny) and IS_IN(nx):
            q.append((ny, nx))

print("HaruHaru") if is_arrive else print("Hing")