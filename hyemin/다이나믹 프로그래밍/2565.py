# 2565

N = int(input())

lines = []

for i in range(N):
    x, y = map(int, input().split())
    lines.append((x, y)) # 튜플 원소로 이루어진 리스트 생성

lines.sort(key = lambda x:x[0])

dp_len = [1] * N

for i in range(1, N):
    for j in range(i):
        if lines[i][1] > lines[j][1]: # 새로운 증가 부분 수열 생성 가능
            dp_len[i] = max(dp_len[i], dp_len[j] + 1) # 단, 이전에 검사했던 부분 수열이 더 클 수 있으니 max를 통해 값을 뽑음

print(str(N - max(dp_len)))