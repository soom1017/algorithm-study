# 트리를 서브 트리로 dp

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline 

N = int(input())
graph  = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N+1)]
# dp[x, 0]: 자신이 얼리어답터가 아닌 경우
# dp[x, 1]: 자신이 얼리어답터인 경우

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(cur_node):
    visited[cur_node] = True
    dp[cur_node][0] = 0
    dp[cur_node][1] = 1

    for node in graph[cur_node]:
        if not visited[node]:
            dfs(node)
            dp[cur_node][0] += dp[node][1]
            dp[cur_node][1] += min(dp[node][0], dp[node][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))