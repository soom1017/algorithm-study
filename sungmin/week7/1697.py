from collections import deque

INF = pow(10, 5)

N, K = map(int, input().split())
dist = [0] * (INF + 1)
move = lambda x: [x - 1, x + 1, x * 2]

def bfs():
    q = deque()
    q.append(N)
    while  q:
        point = q.popleft()
        if point == K: return dist[point]
        for next in move(point):
            if 0 <= next <= INF and not dist[next]:
                dist[next] = dist[point] + 1
                q.append(next)

print(bfs())