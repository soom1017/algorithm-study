'''
탑을 스택에 넣음
~~스택에 넣을 때마다 어차피 9 8 이런식으로 있으면 2~4는 무시됨~~

스택에 넣으면서 나보다 작은 애는 빼다가 큰거 나오면 거기 부딪힘
나와 내가 부딪힌 큰것만 유지
'''
import sys
input = sys.stdin.readline

top_stack = []

N = int(input())
laser_tops = list(map(int, input().split()))
top_stack = []
results = [0] * N

for top_idx in range(N):
    # 만나는 높이가 같거나
    # 더 높은 탑에서 수신 가능
    while top_stack:
        if laser_tops[top_stack[-1][0]] < laser_tops[top_idx]:
            top_stack.pop()
        else:
            results[top_idx] = top_stack[-1][0] + 1
            break
    top_stack.append((top_idx, laser_tops[top_idx]))

for r in results:
    print(r, end=' ')