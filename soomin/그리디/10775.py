# 공항: https://www.acmicpc.net/problem/10775
# Python3로 돌려야 함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
data = [int(input()) for _ in range(p)]

def find_parent(parent, v):
    if parent[v] == v:
        parent[v] = v-1
        return v
    parent[v] = parent[parent[v]]
    return find_parent(parent, parent[v])

result = 0
for d in data:
    if find_parent(parent, d) == 0:
        break
    result += 1

print(result)