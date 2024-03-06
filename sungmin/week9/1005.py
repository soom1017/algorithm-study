from collections import deque
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    COST = [0] + list(map(int, input().split()))
    
    graph = [list() for _ in range(N + 1)]
    to_edges = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        to_edges[b] += 1
    target = int(input())
    
    cost = [0] * (N + 1)
    q = deque()
    for i in range(1, N + 1):
        if not to_edges[i]:
            q.append(i)
            cost[i] = COST[i]

    while q:
        c = q.popleft()
        for next in graph[c]:
            cost[next] = max(cost[next], cost[c] + COST[next])

            to_edges[next] -= 1
            if not to_edges[next]:
                q.append(next)

        if not to_edges[target]:
            break
    
    print(cost[target])