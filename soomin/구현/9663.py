# N-Queen: https://www.acmicpc.net/problem/9663
n = int(input())

result = 0
placed_cols = [-1] * n

def place_ith_queen(i: int):
    global result
    if i == n:
        result += 1
        return
    
    for j in range(n):
        placed_cols[i] = j
        if promising(i):
            place_ith_queen(i+1)
    
'''
백트래킹
- 이전에 놓은 퀸과 충돌하는지 확인하여, 해당하는 경우 더이상 진행하지 않는다.
'''
def promising(i):
    for prev in range(i):
        if (placed_cols[prev] == placed_cols[i]) or (abs(placed_cols[prev] - placed_cols[i]) == i - prev):
            return False
    return True
    
place_ith_queen(0)
print(result)