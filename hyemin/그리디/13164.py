import sys
input = sys.stdin.readline

N, K = map(int, input().split())

heights = list(map(int, input().split()))

heights.sort()

diff = []

for i in range(N - 1):
    diff.append(heights[i + 1] - heights[i])

diff.sort()

print(sum(diff[0:(N-K)]))