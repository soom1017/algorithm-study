# 거짓말: https://www.acmicpc.net/problem/1043
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
knows = set(input().split()[1:])

parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))
# 분리집합 대신 집합으로 풀 경우, 파티 개수(m)만큼 반복 필요.
for _ in range(m):
    for pt in parties:
        if pt & knows:
            knows = knows.union(pt)

result = 0
for pt in parties:
    if pt & knows:
        continue
    result += 1

print(result)