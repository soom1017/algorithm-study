import heapq
N = int(input())

sched = [list(map(int, input().split())) for _ in range(N)]
sched.sort()

end_time = [sched[0][1]]
for sch in sched[1:]:
    if sch[0] >= end_time[0]:
        heapq.heappop(end_time)
    heapq.heappush(end_time, sch[1])
print(len(end_time))