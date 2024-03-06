import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

diff = []

for i in range(N - 1):
    diff.append(sensors[i + 1] - sensors[i])

diff.sort()

print(sum(diff[0:(N-K)]))