# 0306

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    dp = []

    dp.append((1, 0))
    dp.append((0, 1))
    
    for i in range(2, N+1):
        dp.append((dp[i - 1][0] + dp[i-2][0], dp[i - 1][1] + dp[i-2][1]))
    
    print(str(dp[N][0]) + " " + str(dp[N][1]))