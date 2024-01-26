# 치킨 배달: https://acmicpc.net/problem/15686
from itertools import combinations

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))
          
min_value = float('inf')  
for ch in combinations(chicken, m):
    sum_value = 0
    for h in house:
        # 각 집마다 치킨 거리 구하기
        sum_value += min([abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in ch])
        # 지금까지의 누적 치킨 거리가 min_value보다 크다면 바로 다른 조합 찾기. (백트래킹)
        if sum_value >= min_value:
            break
    if sum_value < min_value:
        min_value = sum_value
print(min_value)