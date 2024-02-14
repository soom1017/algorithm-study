from collections import deque

node_num, edge_num, start = map(int, input().split())
graph = [list() for _ in range(node_num + 1)]

for _ in range(edge_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph: edges.sort()

def bfs(): # queue
    q = deque()
    ret = list()
    visit = [0] * (node_num + 1)

    q.append(start)
    while(q):
        node = q.popleft()
        if visit[node]: continue
        visit[node] = 1
        ret.append(node)
        for next in graph[node]:
            q.append(next)

    return ret

def dfs(): # stack
    q = list()
    ret = list()
    visit = [0] * (node_num + 1)

    q.append(start)
    while(q):
        node = q.pop()
        if visit[node]: continue
        visit[node] = 1
        ret.append(node)
        for next in reversed(graph[node]):
            q.append(next)

    return ret

dfs_ret = dfs()
bfs_ret = bfs()

for node in dfs_ret:
    print(node, end=' ')
print()
for node in bfs_ret:
    print(node, end=' ')
print()