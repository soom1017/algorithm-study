# 녹색 옷 입은 애가 젤다지?: https://acmicpc.net/problem/4485
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]            

def case_dijkstra(n: int):
    graph = [list(map(int, input().split())) for _ in range(n)]
    in_graph = lambda x, y: 0 <= x < n and 0 <= y < n
    
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))    # (cost, row, col)
    
    while q:
        dist, row, col = heapq.heappop(q)
        if distance[row][col] < dist:
            continue
    
        for i in range(4):
            new_row, new_col = row + dx[i], col + dy[i]
            if in_graph(new_row, new_col):
                # 지금까지의 루피 + new 장소의 도둑루피가 더 작다면, 업데이트
                cost = dist + graph[new_row][new_col]
                
                if cost < distance[new_row][new_col]:
                    distance[new_row][new_col] = cost
                    heapq.heappush(q, (cost, new_row, new_col))
                    
    return distance[n-1][n-1]

count = 0
while True:
    count += 1
    n = int(input())
    if n == 0:
        break
    
    result = case_dijkstra(n)
    print(f"Problem {count}: {result}")