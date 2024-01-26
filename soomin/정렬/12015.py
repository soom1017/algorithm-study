# 가장 긴 증가하는 부분 수열 2: https://acmicpc.net/problem/12015
from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))

# 증가하는 부분 수열 임시 저장
d = [0]

for e in A:
    if d[-1] < e:
        d.append(e)
    else:
        idx = bisect_left(d, e)
        d[idx] = e

print(len(d) - 1)