import sys, heapq
input = sys.stdin.readline

INF = 1e9
N = int(input())
M = int(input())
EDGES = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    EDGES[a].append((b, c))

distance = [INF] * (N + 1)

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

S, E = map(int, input().split())
dijkstra(S)
print(distance[E])