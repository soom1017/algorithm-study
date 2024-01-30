# 2579

'''
n번째 계단에 오를 수 있는 경우.

1. stair[n-1]을 찍고 1칸 올라 stair[n]에 온 경우: n-1과 n은 연속되므로 n-1을 찍기 전엔 n-3을 찍었어야 한다. 즉 n-3까지 도달하기 위한 최댓값 + s[n-1] + s[n]
2. stair[n-2]를 찍고 2칸 올라 stair[n]에 온 경우: n-2과 n은 불연속이므로 n-2까지 도달하기 위한 최댓값 + s[n]
'''

N = int(input())

stairs = [0] * 301

for i in range(N):
    stairs[i] = int(input())

# 계단의 개수는 300이하의 자연수이기 때문에, dp0~2를 초기화할 때 계단의 개수가 1 이하인 경우 OOB가 발생할 수 있다
# 따라서, stairs와 dp 배열을 초기화할 때 max length인 301로 미리 초기화해주어야 한다.
dp = [0] * 301
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0], stairs[1]) + stairs[2]

for n in range(3, N):
    dp[n] = max(stairs[n] + stairs[n-1] + dp[n-3], stairs[n] + dp[n-2])

print(dp[N-1])