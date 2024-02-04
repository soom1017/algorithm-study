# 백준 11054
# 바이토닉 부분수열 : 수열에서 어떤 위치를 기준으로 그 위치까지는 증가하다가 그 이후 감소하는 부분수열

n = int(input())

arr = list(map(int, input().split()))

dp1 = [1]*n # 각 원소를 마지막으로 하는 증가하는 부분수열의 최대 길이 저장
dp2 = [1]*n # 각 원소를 시작으로 하는 감소하는 부분수열의 최대 길이 저장

# dp1, dp2 계산
for k in range(n):
    for i in range(k):
        for j in range(i):
            if arr[j] < arr[i]:
                dp1[i] = max(dp1[i], dp1[j]+1)

    for i in range(n-1, k-1, -1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                dp2[i] = max(dp2[i], dp2[j]+1)

# 각 위치에서의 dp1과 dp2의 합을 저장
dp3 = [0]*n

for i in range(n):
    dp3[i] = dp1[i] + dp2[i]
print(max(dp3)-1)