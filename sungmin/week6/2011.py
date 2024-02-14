DIV = 1000000
ss = list(map(int, list(input())))
if ss[0] == 0: print(0)
else:
    dp = [0] * (len(ss) + 1)
    dp[0], dp[1] = 1, 1

    for i in range(1, len(ss)):
        if ss[i] > 0:
            dp[i + 1] += dp[i]
        if 10 <= ss[i] + ss[i - 1] * 10 <= 26:
            dp[i + 1] += dp[i - 1]
        
    print(dp[len(ss)] % DIV)
