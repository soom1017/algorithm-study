import sys
sys.setrecursionlimit(100000)

N = int(input())
tree = [list() for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
weight = [0] * (N+1)
max_diameter = 0

def dp(c):
    global max_diameter
    
    if not tree[c]: return 0 # leaf node
    if weight[c]: return weight[c]
    
    rlist = [dp(n) + w for n, w in tree[c]]
    max_diameter = max(max_diameter, sum(sorted(rlist, reverse=True)[:2]))

    for w in rlist: weight[c] = max(weight[c], w)
    return weight[c]
dp(1)

print(max_diameter)