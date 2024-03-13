import heapq
INF = 10e9
N, M, X = map(int, input().split())

graph = [list() for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

def bfs(n): # n에서 다른 노드까지의 최단 거리
    q = list()
    visited = [0] * (N + 1)
    distance = [INF] * (N + 1)
    
    heapq.heappush(q, (0, n))
    while q:
        curr_time, node = heapq.heappop(q)
        if visited[node]: continue
        visited[node] = 1
        distance[node] = curr_time
        for next_time, next in graph[node]:
            heapq.heappush(q, (min(curr_time + next_time, distance[next]), next))
    return distance

distances = list([list()])
for n in range(1, N + 1):
    distances.append(bfs(n))

ret = list()
for n in range(1, N + 1):
    ret.append(distances[n][X] + distances[X][n])

print(max(ret))