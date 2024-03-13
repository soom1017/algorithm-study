import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [list() for _ in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def DP(curr:int, is_early:bool, parent=None):
    ret = 0
    for friend in graph:
        print(curr, is_early, parent=None)
        if parent and friend == parent: continue
        ret += DP(friend, not is_early, curr)
    return ret

print(min(DP(1, True), DP(1, False)))
