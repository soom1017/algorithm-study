# 2048 (Easy): https://www.acmicpc.net/problem/12100
import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

'''
한번 이동.
'''
def run_once(direction: int, board: list):
    # direction: 0 (left), 1 (right), 2 (up), 3 (down)
    if direction == 0:
        # left
        for row in range(n):
            left_idx = 0
            for col in range(1, n):
                if board[row][col]:
                    found = board[row][col]
                    board[row][col] = 0
                                        
                    if board[row][left_idx] == 0:
                        board[row][left_idx] = found
                    elif board[row][left_idx] == found:
                        board[row][left_idx] *= 2
                        left_idx += 1
                    else:
                        left_idx += 1
                        board[row][left_idx] = found
    elif direction == 1:
        # right
        for row in range(n):
            right_idx = n-1
            for col in range(n-2, -1, -1):
                if board[row][col]:
                    found = board[row][col]
                    board[row][col] = 0
                                        
                    if board[row][right_idx] == 0:
                        board[row][right_idx] = found
                    elif board[row][right_idx] == found:
                        board[row][right_idx] *= 2
                        right_idx -= 1
                    else:
                        right_idx -= 1
                        board[row][right_idx] = found
    elif direction == 2:
        # up
        for col in range(n):
            top_idx = 0
            for row in range(1, n):
                if board[row][col]:
                    found = board[row][col]
                    board[row][col] = 0
                                        
                    if board[top_idx][col] == 0:
                        board[top_idx][col] = found
                    elif board[top_idx][col] == found:
                        board[top_idx][col] *= 2
                        top_idx += 1
                    else:
                        top_idx += 1
                        board[top_idx][col] = found
    else:
        # down
        for col in range(n):
            bottom_idx = n-1
            for row in range(n-2, -1, -1):
                if board[row][col]:
                    found = board[row][col]
                    board[row][col] = 0
                                        
                    if board[bottom_idx][col] == 0:
                        board[bottom_idx][col] = found
                    elif board[bottom_idx][col] == found:
                        board[bottom_idx][col] *= 2
                        bottom_idx -= 1
                    else:
                        bottom_idx -= 1
                        board[bottom_idx][col] = found
    return board

'''
5번 이동하는 모든 경우의 수 계산.
- DP로 풀기엔 memorize size가 커서 (모든 경우에 대해 board 저장) 메모리 초과 예상
- 따라서 재귀로 풀이
'''    
def run(count: int, board: list):
    global result
    if count == 5:
        # update result, if better
        max_in_board = 0
        for line in board:
            max_in_board = max(max(line), max_in_board)
        
        result = max(max_in_board, result)
        return
    
    # if 0 <= count < 5, run once on all directions
    for direction in range(4):
        next_board = run_once(direction, deepcopy(board))
        run(count + 1, next_board)    

result = 0
run(0, board)

print(result)