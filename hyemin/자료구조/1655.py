import heapq
import sys

input = sys.stdin.readline

N = int(input().rstrip())
max_heap = []
min_heap = []

for _ in range(N):
    num = int(input().rstrip())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num) # -를 곱해서 max heap이 되게 함
    else:
        heapq.heappush(min_heap, num)

    # 교체가 필요한 경우 교체함
    if len(min_heap) >= 1 and -max_heap[0] > min_heap[0]:
        max_root = heapq.heappop(max_heap)
        min_root = heapq.heappop(min_heap)

        heapq.heappush(min_heap, -max_root)
        heapq.heappush(max_heap, -min_root)
    
    print(-max_heap[0])