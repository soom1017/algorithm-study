import sys
input = sys.stdin.readline

N, M = map(int, input().split())
D = {}

for _ in range(N):
    url, pw = input().split()
    D[url] = pw

for _ in range(M):
    print(D[input()[:-1]])
