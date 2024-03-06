from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    queue = deque()
    queue.append(dots[0]) # home
    visited = [False for _ in range(n+2)]

    while queue:
        x, y = queue.popleft()

        if abs(x - dots[n+1][0]) + abs(y - dots[n+1][1]) <= 1000: # 도착한 경우
            print("happy")
            return

        for k in range(1, n+1):
            if not visited[k]:
                nx, ny = dots[k]
                if abs(x - nx) + abs(y - ny) <= 1000: # 도착한 경우
                    queue.append(dots[k])
                    visited[k] = True
    
    print("sad") # 도달 실패
    return

for _ in range(int(input())):
    n = int(input())
    dots = []

    for i in range(n+2):
        ix, iy = map(int, input().split())
        dots.append((ix, iy))

    bfs(n)