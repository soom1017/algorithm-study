# 야매적으로, 될 것 같은데? 하고 푼 문제이다. 제대로 검색해서 정당성을 이해하자
# https://goodbyeanma.tistory.com/66

import sys, heapq
input = sys.stdin.readline

INF = 1e9

N, M, K = map(int, input().split())
EDGES = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    EDGES[a].append((b, c))

distance = [[INF] * (K) for _ in range(N + 1)]

def dijkstra(start):
    q = []
    distance[start][0] = 0
    heapq.heappush(q, (0, start)) # 첫번째 원소가 정렬 기준
    while q:
        cost, now = heapq.heappop(q)
        if distance[now][K - 1] < cost: continue
        
        for dest, ncost in EDGES[now]:
            _cost = cost + ncost
            if _cost >= distance[dest][K - 1]: continue
            distance[dest][K - 1] = _cost
            distance[dest].sort()
            heapq.heappush(q, (_cost, dest)) # 첫번째 원소가 정렬 기준

dijkstra(1)
for dist in distance[1:]:
    dist.sort()
    if dist[K-1] == INF: print(-1)
    else: print(dist[K-1])