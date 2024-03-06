import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
qmax, qmin = [], []

for _ in range(N):
    n = int(input().rstrip())
    
    if len(qmax) <= len(qmin):
        heapq.heappush(qmax, -n)
    else:
        heapq.heappush(qmin, n)

    if qmin and -qmax[0] > qmin[0]:
        _max = -heapq.heappop(qmax)
        _min = heapq.heappop(qmin)
        
        heapq.heappush(qmax, -_min)
        heapq.heappush(qmin, _max)

    print(-qmax[0])
