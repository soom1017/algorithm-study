# 특정한 최단 경로: https://www.acmicpc.net/problem/1504
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# v1, v2에 대해 다익스트라 쓰고, v1 ~ v2 + min(1 ~ v1 + v2 ~ N, 1 ~ v2 + v1 ~ N) 계산하기
def dijkstra(start):
    distance = [INF] * (v+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i, w in graph[now]:
            cost = dist + w
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    
    return distance

v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

result = v1_dist[v2] + min(v1_dist[1] + v2_dist[v], v2_dist[1] + v1_dist[v])
print(result if result < INF else -1)