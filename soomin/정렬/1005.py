import sys
input = sys.stdin.readline

t = int(input())
n, k = map(int, input().split())

time_build = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x] = y