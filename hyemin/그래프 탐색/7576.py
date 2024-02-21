import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes_matrix = []
queue = deque([])

for i in range(N):
    # 1: 익은 토마토
    # 0: 안익은 토마토
    # -1: 토마토가 없음
    tomato_row = list(map(int, input().split()))

    for j in range(M):
        if tomato_row[j] == 1:
            queue.append([i, j]) # 익은 토마토 전부 저장

    tomatoes_matrix.append(tomato_row)

# 익은 토마토를 중심으로 상하좌우 토마토를 익혀줌
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue: # queue에서 익은 토마토를 꺼냄
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if tomatoes_matrix[nx][ny] == 0:
                tomatoes_matrix[nx][ny] = tomatoes_matrix[x][y] + 1 # 며칠 지났는지 확인하는 용도 -> 전파원에서 1을 더함
                queue.append([nx, ny])
            
result = 0

for row in tomatoes_matrix:
    for tomato in row:
        if tomato == 0: # 안 익은 토마토 존재
            print(-1)
            exit(0)
    result = max(result, max(row))

print(result - 1)