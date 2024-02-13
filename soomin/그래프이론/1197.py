# 최소 스패닝 트리: https://www.acmicpc.net/problem/1197
import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
    
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, (cost, a, b))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    x1 = find_parent(parent, a)
    x2 = find_parent(parent, b)
    if x1 > x2:
        parent[x1] = x2
    else:
        parent[x2] = x1
        
result = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)