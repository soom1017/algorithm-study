# 연속합: https://www.acmicpc.net/problem/1912
n = int(input())
d = list(map(int, input().split()))

for i in range(1, n):
    # i번째까지의 최댓값: d[i]
    d[i] = max(d[i], d[i-1] + d[i])

print(max(d))