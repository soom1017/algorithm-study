# 쉬운 계단 수: https://www.acmicpc.net/problem/10844
N = int(input())
mod = 1000000000

dp = [[0] * 10 for _ in range(N+1)] # dp[length][마지막 num]: 경우의 수
                                    # dp[마지막 num]으로 하고, 매 반복마다 dp = dp_next해도 됨.
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

print(sum(dp[N]) % mod)