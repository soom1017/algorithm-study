# 보석 도둑: https://acmicpc.net/problem/1202
import sys
import heapq

read = sys.stdin.readline # input vs readline: https://hs-archive.tistory.com/35
n, k = map(int, read().split())

jewels = []
for _ in range(n):
    # 보석 무게에 대한 최소 힙
    m, v = map(int, read().split())
    heapq.heappush(jewels, (m, v))    
weight_bags = [int(read()) for _ in range(k)]

result = 0

# 가방은 작은 것부터 채우기
weight_bags.sort()

avaiable_jewels = []
for weight in weight_bags:
    # 가벼운 보석부터, 가방에 들어갈 수 있는 것까지만 보석 가격에 대한 최대 힙에 넣기
    while jewels and jewels[0][0] <= weight:
        jewel = heapq.heappop(jewels)
        heapq.heappush(avaiable_jewels, -jewel[1])
    
    if avaiable_jewels:
        result -= heapq.heappop(avaiable_jewels)
        
print(result)