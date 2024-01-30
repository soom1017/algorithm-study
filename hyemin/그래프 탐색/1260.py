from collections import deque

# input 받기

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N + 1):
    graph[i].sort()

# dfs 출력
def dfs(start):
    if not visited[start]:
        print(start, end=' ')
        visited[start] = True
        for node in graph[start]:
            dfs(node)

dfs(V)

print()

visited = [False] * (N + 1) 

# bfs 결과 출력

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

bfs(V)