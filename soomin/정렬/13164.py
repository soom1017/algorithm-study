# 행복 유치원: https://acmicpc.net/problem/13164
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

intervals = [kids[i] - kids[i-1] for i in range(1, n)]
intervals.sort()

# 간격 중 큰 간격 k개 제거
result = sum(intervals[:n-k])
print(result)