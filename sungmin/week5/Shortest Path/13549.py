import sys, heapq
input = sys.stdin.readline

INF = 1e9
X = 100001

N, K = map(int, input().split())
EDGES = [[] for _ in range(X)]
for i in range(X):
    if 0 <= i - 1 < X: EDGES[i].append((i - 1, 1))
    if 0 <= i + 1 < X: EDGES[i].append((i + 1, 1))
    if 0 <= i * 2 < X: EDGES[i].append((i * 2, 0))

distance = [INF] * (X)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0))
    while q:
        now, cost = heapq.heappop(q)
        if distance[now] < cost: continue
        
        for dest, cost in EDGES[now]:
            cost += distance[now]
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (dest, cost))

dijkstra(N)
print(distance[K])