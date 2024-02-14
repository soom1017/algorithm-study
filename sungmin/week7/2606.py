node_num, edge_num = int(input()), int(input())

graph = [list() for _ in range(node_num + 1)]
for _ in range(edge_num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = list()
visit = [0] * (node_num + 1)

q.append(1)
while(q):
    node = q.pop()
    if visit[node]: continue
    visit[node] = 1
    
    for next in graph[node]:
        q.append(next)

count = 0
for i in visit:
    if i: count += 1
print(count - 1)