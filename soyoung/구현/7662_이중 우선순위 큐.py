import sys, bisect
from collections import deque, defaultdict
 
for _ in range(int(sys.stdin.readline().strip())):
    li = deque()
    cnt = defaultdict(int)
    for _ in range(int(sys.stdin.readline().strip())):
        a,b = sys.stdin.readline().strip().split()
        if a == "I":
            if cnt[int(b)]:
                cnt[int(b)] += 1
            else:
                bisect.insort(li, int(b))
                cnt[int(b)] = 1
        else:
            if int(b) == 1 and li:
                cnt[li[-1]] -= 1
                if not cnt[li[-1]]:
                    li.pop()
            elif int(b) == -1 and li:
                cnt[li[0]] -= 1
                if not cnt[li[0]]:
                    li.popleft()
    if li:
        print(li[-1], li[0])
    else:
        print("EMPTY")