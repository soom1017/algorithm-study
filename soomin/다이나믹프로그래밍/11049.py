# 행렬 곱셈 순서: https://acmicpc.net/problem/11049
import sys

INF = sys.maxsize

n = int(input())

# 행렬이 p1 X p2, p2 X p3, ... 일 때, mat: [p1, p2, p3, ...]
mat = []
for _ in range(n):
    r, c = map(int, input().split())
    mat.append(r)
mat.append(c)

# d[i][j]: i번째 행렬 ~ j번째 행렬의 곱의 최소 scalar multiplication 수
# d[i][j] = d[i][k] + d[k+1][j] + mat[i-1]mat[k]mat[j]
d = [[0] * n for _ in range(n)]

for l in range(2, n+1):     # l: 행렬 몇 개 (length) 곱한 것의 결과인지
    for i in range(n-l+1):
        j = i + l - 1
        d[i][j] = INF
        for k in range(i, j):
            q = d[i][k] + d[k+1][j] + mat[i-1] * mat[k] * mat[j]
            if q < d[i][j]:
                d[i][j] = q

print(d[0][n-1])