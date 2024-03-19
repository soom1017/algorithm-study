# 골드2

import sys
import heapq
input=sys.stdin.readline

N, K = map(int,input().split())

jewels = []

for _ in range(N):
    M, V = map(int,input().split()) 
    jewels.append((M, V))

bags = [int(input()) for _ in range(K)]

jewels.sort(reverse=True) # 무게 기준으로 정렬(내림차순)
bags.sort() # 오름차순 정렬

result = 0
heap = []

for bag in bags:
    while jewels and bag >= jewels[-1][0]: # 가방 무게가 보석 최소 무게보다 큰 경우
        weight, value = jewels.pop()
        heapq.heappush(heap, -value) # 최대힙에 push
    
    if len(heap) != 0:
        result -= heapq.heappop(heap) # 가장 가치가 큰 값을 결과에 더해줌

print(result)