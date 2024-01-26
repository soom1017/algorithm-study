# 별 찍기 - 18: https://acmicpc.net/problem/10993
n = int(input())

height = 2**n - 1
triangle = [[False] * height for _ in range(height)]

def forward(triangle, start, n):
    height = 2**n - 1
    for i in range(height - 1):
        triangle[start + i][i] = True
    for i in range(height):
        triangle[start + height - 1][i] = True
    if n != 1:
        reverse(triangle, start + height // 2, n-1)

def reverse(triangle, start, n):
    height = 2**n - 1
    for i in range(height):
        triangle[start][i] = True
    for i, j in enumerate(range(height - 1, 0, -1)):
        triangle[start + j][i] = True
    forward(triangle, start + 1, n-1)
    
if n % 2 == 0:
    reverse(triangle, 0, n)
else:
    forward(triangle, 0, n)
    
for i in range(height):
    line = ''
    if n != 1:
        for star in triangle[i][1:][::-1]:
            line += '*' if star else ' '
    for star in triangle[i][:]:
        line += '*' if star else ' '
    line = line.rstrip()  # 오른쪽 공백으로 인한 '출력 형식이 잘못되었습니다' 에러 방지
    print(line + ' ' if i != height - 1 else line)