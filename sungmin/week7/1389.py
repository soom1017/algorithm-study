INF = 1e9
N, M = map(int, input().split())
graph =[[INF] * (N + 1)  for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1
for i in range(1, N + 1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1 , N + 1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

_min, ret = INF, 0
for i in range(N, 0, -1):
    s = sum(graph[i][1:]) # 케빈 베이컨
    if _min >= s: _min, ret = s, i
print(ret)