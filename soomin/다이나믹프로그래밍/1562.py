# 계단 수: https://www.acmicpc.net/problem/1562
N = int(input())
mod = 1000000000

dp = [[0 for _ in range(1<<10)] for _ in range(10)] # dp[마지막 num][10bits]: 경우의 수
for i in range(1, 10):
    dp[i][1 << i] = 1

for i in range(1, N):
    dp_next = [[0 for _ in range(1<<10)] for _ in range(10)]
    for j in range(10):
        for k in range(1<<10):
            if j == 0:
                dp_next[j][k | (1 << j)] += dp[1][k]
            elif j == 9:
                dp_next[j][k | (1 << j)] += dp[8][k]
            else:
                dp_next[j][k | (1 << j)] += dp[j-1][k]
                dp_next[j][k | (1 << j)] += dp[j+1][k]
            dp_next[j][k | (1 << j)] %= mod
    dp = dp_next
    
sum = 0
for i in range(10):
    sum += (dp[i][1023] % mod)
print(sum % mod)