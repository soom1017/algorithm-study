def find(a,b): # 탐색
    visited[a][b] = 1
    queue = deque()
    queue.append([a,b])
    while queue:
        y, x = queue.popleft()
        for dy, dx in move :
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if color[ny][nx] == color[y][x]:
                    visited[ny][nx] = 1
                    queue.append([ny,nx])

def check(): # 볼 수 있는 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                find(i,j)
                cnt += 1
    return cnt

import sys
from collections import deque
move = [[0,1],[0,-1],[1,0],[-1,0]]
N = int(sys.stdin.readline())
color = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result = check()

#적록색약
visited = [[0]*N for _ in range(N)] # 방문 체크 초기화
for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'
rgresult = check()
print(result, rgresult)