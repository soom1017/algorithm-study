# 1504: 특정한 최단 경로

import heapq
INF = int(1e9)

# 데이터 입력 받기

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)] # 노드에 연결되어 있는 간선 정보를 담는 그래프 생성

for _ in range(E): # 간선 정보 입력 받기
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w)) # v1 노드로부터 v2 노드까지 가중치 w를 가진다.
    graph[v2].append((v1, w)) # 양방향 그래프

def dijkstra(start):
    min_dist = [INF] * (V + 1) # 최단 거리를 담는 리스트 (INF 값으로 초기화)
    q = []

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
    heapq.heappush(q, (0, start))
    min_dist[start] = 0

    while q:
        now_dist, now_node = heapq.heappop(q) # 최단 거리가 가장 짧은 노드 정보 꺼내기
        if min_dist[now_node] >= now_dist: # 뽑은 dist가 이전에 저장된 거리보다 짧은 경우
            for next_node in graph[now_node]: # 인접한 노드를 확인
                cost = now_dist + next_node[1] # 현재 노드를 거쳐서 인접한 노드로 이동하는 경우에 대한 cost 계산 
                if cost < min_dist[next_node[0]]: # 해당 cost가 기존에 저장된 최단 거리보다 더 짧은 경우
                    min_dist[next_node[0]] = cost
                    heapq.heappush(q, (cost, next_node[0])) # 우선순위 큐의 데이터 갱신
    
    return min_dist

v1, v2 = map(int, input().split())
                    
ori_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

path1 = ori_dist[v1] + v1_dist[v2] + v2_dist[V]
path2 = ori_dist[v2] + v2_dist[v1] + v1_dist[V]

result = min(path1, path2)

print(result if result < INF else -1)