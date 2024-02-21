import heapq # min heap
import sys

input = sys.stdin.readline

N = int(input().strip()) # 연산 횟수

heap = []

for _ in range(N):
    x = int(input().strip())

    if x == 0: # 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거
        max_x = 0
        if len(heap) > 0:
            max_x = heapq.heappop(heap)
        print(-max_x)
    else: # 배열에 x값을 넣음
        heapq.heappush(heap, -x)