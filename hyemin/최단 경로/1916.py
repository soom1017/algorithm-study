import sys
import heapq

# 1. input 처리

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

buses_graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1) # 최단 거리를 저장하는 테이블

for _ in range(M):
    start, dest, dist_cost = map(int, input().split())
    buses_graph[start].append((dest, dist_cost))

start, dest = map(int, input().split())

# 다익스트라 알고리즘 구현

def dijkstra(start_node):
    queue = [] # 우선순위 큐
    heapq.heappush(queue, (0, start_node)) # 시작 노드에 대한 최단 경로를 0으로 설정하여 큐에 삽입
    distance[start_node] = 0

    while queue: # 큐가 비어있지 않을 때까지 수행
        dist, now = heapq.heappop(queue)

        if dist <= distance[now]: # 현재까지 기록된 최단 거리보다 큐에서 꺼낸 dist가 짧은 경우 갱신 수행
            for next_node, next_cost in buses_graph[now]: # data: (dest, cost 형태)
                cost = dist + next_cost
                if distance[next_node] > cost:
                    distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))

dijkstra(start)
print(distance[dest])