# 강의실 배정: https://acmicpc.net/problem/11000
import sys
import heapq

input = sys.stdin.readline

n = int(input())

classes = []
for _ in range(n):
    a, b = map(int, input().split())
    classes.append((a, b))

# 수업 시작시간으로 정렬
classes.sort(key=lambda x: x[0])
    
# 각 강의실의 수업 끝나는 시간만 저장할 큐
rooms = []
heapq.heappush(rooms, classes[0][1])

for i in range(1, n):
    if rooms[0] <= classes[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, classes[i][1])

print(len(rooms))