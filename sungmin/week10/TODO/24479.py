# N, M, R = map(int, input().split())

# graph = [list() for _ in range(N + 1)]
# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# for l in graph: l.sort()
# visit = [0] * (N + 1)

# def dfs():
#     q = list()
#     q.append(R)
#     while q:
#         u = q.pop()
#         if visit[u]: continue
#         visit[u] = 1
#         print(u)
        
#         for v in graph[u]:
#             q.append(v)

# dfs()