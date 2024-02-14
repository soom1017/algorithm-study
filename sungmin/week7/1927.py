import sys, heapq

input = sys.stdin.readline

N = int(input().rstrip())
q = list()

for _ in range(N):
    num = int(input().rstrip())

    if num != 0:
        heapq.heappush(q, num)
    else:
        try:
            print(heapq.heappop(q))
        except:
            print(0)