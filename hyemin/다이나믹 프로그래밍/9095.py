import sys
input = sys.stdin.readline

'''
숫자 N이 주어졌을 때,

1 + (N - 1)
2 + (N - 2)
3 + (N - 3)

으로 조합이 가능함.

즉, dp[N] = dp[N-1] + dp[N-2] + dp[N-3]
'''

T = int(input())

for _ in range(T):
    n = int(input().strip())

    if n <= 3:
        print(2**(n-1))
        continue

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    print(dp[n])