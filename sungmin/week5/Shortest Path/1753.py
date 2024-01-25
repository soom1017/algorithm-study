import sys, heapq
input = sys.stdin.readline

INF = 1e9
V, E = map(int, input().split())
K = int(input())
# 괜히 EDGES V^2 2차원 배열로 설정했다가 몇번씩이나 틀림
# 그냥 힙 테이블로 쓰는게 맞음
EDGES = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    EDGES[a].append((b, c))

distance = [INF] * (V + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost: continue
        
        for dest, cost in EDGES[now]:
            cost = cost + distance[now]
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(q, (cost, dest))

dijkstra(K)
for d in distance[1:]:
    if d == INF: print("INF")
    else: print(d)
