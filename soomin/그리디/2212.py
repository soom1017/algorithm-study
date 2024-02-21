# 센서: https://www.acmicpc.net/problem/2212
n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

dist = []
for i in range(0, n-1):
    dist.append(sensors[i+1] - sensors[i])

dist.sort(reverse=True)

result = 0
for i in range(k-1, n-1):
    result += dist[i]

print(result)