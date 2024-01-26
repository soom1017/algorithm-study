# 파티: https://acmicpc.net/problem/1238
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        
        for node, edge in graph[now]:
            cost = dist + edge
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance

result = 0

back = dijkstra(x)      # back: x에서 출발, 돌아오는 거리
for i in range(1, n+1):
    go = dijkstra(i)    # go: i에서 출발, 가는 거리
    result = max(result, go[x] + back[i])
    
print(result)