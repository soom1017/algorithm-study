import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

#v는 정점 수, e는 간선 수, x는 목표 마을
v, e, x = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(v + 1)]


for _ in range(e):
    a, b, cost = map(int, input().split()) # 간선 정보를 입력받기
    graph[a].append((b, cost)) # graph[a]에는 a에서 b로 가는데 소요되는 시간 cost를 저장

# 다익스트라 함수
def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


# 반복문을 사용하여 모든 노드에 대해 파티를 열기 위한 최단 거리를 계산하고, 그 중 최댓값
result = 0

for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)

# 다익스트라 알고리즘, 그래프