import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = list(set([input().rstrip() for _ in range(N)]))
for v in sorted(l, key=lambda x: (len(x), x)):
    print(v)