# 욕심쟁이 판다: https://www.acmicpc.net/problem/1937
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# DP
d = [[0] * n for _ in range(n)]

# 그래프 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
in_graph = lambda x, y: 0 <= x < n and 0 <= y < n

def dfs(x, y):
    if d[x][y]: 
        return d[x][y]
    d[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if in_graph(nx, ny) and graph[x][y] < graph[nx][ny]:
            d[x][y] = max(d[x][y], dfs(nx, ny) + 1)
    return d[x][y]

result = 0
for x in range(n):
    for y in range(n):
        result = max(result, dfs(x, y))

print(result)