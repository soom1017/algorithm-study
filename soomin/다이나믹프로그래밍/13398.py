# 연속합 2: https://www.acmicpc.net/problem/13398
n = int(input())
data = list(map(int, input().split()))

d = data[:]				# i번째까지 (수를 제거하지 않은) 최댓값: d[i]
d_removed = data[:]		# i번째까지 (수를 하나 제거한) 최댓값: d_removed[i]

for i in range(1, n):
    d[i] = max(d[i], d[i-1] + d[i])
    d_removed[i] = max(d[i-1], d_removed[i-1] + data[i])

result = max(max(d), max(d_removed))
print(result)