'''
A~Z에 각각 1~26 번호 부여.
1. 자릿수가 하나인 수에 대해 [1, 9] -> dp[i-1]의 개수와 동일
2. 자릿수가 두개인 수에 대해 [10, 26] -> dp[i-2]의 개수와 동일
'''

code = list(map(int, input()))

if code[0] == 0:
    print("0")
else:
    code_len = len(code)

    dp = [0] * (code_len + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(1, code_len):
        dp_idx = i + 1
        if code[i] > 0: # 한자리
            dp[dp_idx] += dp[dp_idx - 1]
        if 10 <= code[i] + code[i - 1] * 10 <= 26: # 두자리
            dp[dp_idx] += dp[dp_idx - 2]
    
    print(dp[code_len] % 1000000)
