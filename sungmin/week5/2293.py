import sys
input = sys.stdin.readline

N, K = map(int, input().split())
COINS = [int(input()) for _ in range(N)]
COINS.sort()

DP = [0] * (K + 1)

for coin in COINS:
    if coin > K: continue
    index = coin
    DP[index] += 1
    while(index <= K):
        if DP[index - coin]:
            if DP[index]:
                DP[index] = DP[index] + DP[index - coin]
            else:
                DP[index] = DP[index - coin]
        index += 1

print(DP[K])