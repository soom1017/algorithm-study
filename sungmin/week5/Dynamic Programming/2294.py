import sys
input = sys.stdin.readline

INF = 10001
N, K = map(int, input().split())
COINS = [int(input()) for _ in range(N)]
COINS.sort()

DP = [INF] * (K + 1)

for coin in COINS:
    if coin > K: continue
    index = coin
    DP[index] = 1
    while(index <= K):
        if DP[index - coin] != -1:
            if DP[index]:
                DP[index] = min(DP[index], 1 + DP[index - coin])
            else:
                DP[index] = 1 + DP[index - coin]
        index += 1

if DP[K] == INF:
    print(-1)
else:
    print(DP[K])