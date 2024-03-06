n = int(input())
stack = list()
goals = [int(input()) for _ in range(n)]
source = [i for i in range(1, n + 1)]

ret = list()
for goal in goals:
    while source and source[0] <= goal:
        stack.append(source.pop(0))
        ret.append('+')
    if stack[-1] == goal:
        stack.pop(-1)
        ret.append('-')

if stack: print("NO")
else: [print(i) for i in ret]