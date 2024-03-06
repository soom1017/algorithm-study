import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # recursion limit 어떻게 계산?? 

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)
current_order = 1

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for vertex in graph:
    vertex.sort()

def dfs(current_node):
    global current_order

    visited[current_node] = current_order

    for neighbor in graph[current_node]:
        if visited[neighbor] == 0:
            current_order += 1
            dfs(neighbor)

dfs(R)

for i in visited[1:]:
    print(i)