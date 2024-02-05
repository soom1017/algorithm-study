from collections import deque

T = int(input())
D = [(0,1), (1,0), (0,-1), (-1,0)]

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    
    def search(y, x):
        if not (0 <= y < N and 0 <= x < M): return
        if visit[y][x]: return
        
        visit[y][x] = 1

        if graph[y][x]:
            for dy, dx in D:
                ny, nx = dy + y, dx + x
                search(ny, nx)
    
    for y in range(N):
        for x in range(M):
            if not graph[y][x]: continue
            if visit[y][x]: continue
            search(y, x)
            count += 1
    
    print(count)