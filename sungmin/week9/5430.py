from collections import deque
import ast

T = int(input())
for _ in range(T):
    cmd_set = input()
    n = int(input())
    arr = deque(ast.literal_eval(input()))

    reverse = False
    try:
        for c in cmd_set:
            if c == 'R': reverse = False if reverse else True
            if c == 'D': arr.pop() if reverse else arr.popleft()
        if reverse: arr.reverse()
        print(str(list(arr)).replace(" ", ""))
    except:
        print("error")