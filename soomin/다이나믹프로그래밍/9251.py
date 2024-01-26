# LCS: https://acmicpc.net/problem/9251
s = " " + input()
t = " " + input()

d = [[0] * len(t) for _ in range(len(s))]

for i in range(1, len(s)):
    for j in range(1, len(t)):
        # 현재 두 수열의 마지막 문자가 같다면, 두 수열에서 마지막 문자를 제외. 결과에 + 1
        if s[i] == t[j]:
            d[i][j] = d[i-1][j-1] + 1
        # 현재 두 수열의 마지막 문자가 다르다면, 하나의 수열만 마지막 문자 제외.
        else:
            d[i][j] = max(d[i][j-1], d[i-1][j])
            
print(d[-1][-1])