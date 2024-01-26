# 가장 긴 증가하는 부분 수열: https://acmicpc.net/problem/11053
n = int(input())
A = list(map(int, input().split()))

# d[i]: i번째까지 가장 긴 증가하는 부분 수열의 길이. A[i]보다 작거나 같은 놈 (k번째) 찾아서, d[i] = d[k] + 1
d = [1] * n

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            d[i] = max(d[j] + 1, d[i])
            
print(max(d))