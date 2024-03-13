import sys
input = sys.stdin.readline

def nCk(n, k):
    # nCk = (n-1)C(k-1) + (n-1)Ck

    dp = [[0 for i in range(k + 1)] for j in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1 # nC0은 항상 1
    
    for i in range(1, n+1):
        for j in range(1, min(n, k) + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][k]

for _ in range(int(input())):
    N_input, M_input = map(int, input().split())
    print(nCk(M_input, N_input))
    
    # mCn = m!/{n!(m-n)!} = m * (m-1) * ... * (m - n + 1)
    