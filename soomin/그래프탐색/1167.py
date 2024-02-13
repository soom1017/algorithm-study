# 트리의 지름: https://www.acmicpc.net/problem/1167
import sys
sys.setrecursionlimit(int(1e6))

v = int(input())

graph = [[] for _ in range(v+1)]
for _ in range(v):
    data = list(map(int, input().split()))
    
    start = data[0]
    for i in range(1, len(data)-1, 2):
        graph[data[0]].append((data[i], data[i+1]))

def dfs(v, prev_dist):
    for i, w in graph[v]:
        if dist[i] == -1:
            dist[i] = prev_dist + w
            dfs(i, dist[i])


dist = [-1] * (v+1)
dist[1] = 0
dfs(1, 0)

endpoint = dist.index(max(dist))
dist = [-1] * (v+1)
dist[endpoint] = 0
dfs(endpoint, 0)

print(max(dist))