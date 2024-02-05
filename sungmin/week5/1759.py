from itertools import combinations

GATHER = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
charlist = input().split()

combi = list(combinations(charlist, L))
for i, s in enumerate(combi):
    s = list(s)
    s.sort()
    combi[i] = ''.join(s)
combi.sort()
for s in combi:
    gath, cons = 0, 0
    for c in s:
        if c in GATHER:
            gath += 1
        else: cons += 1
    if gath >= 1 and cons >= 2:
        print(s)

# 백트래킹 공부하기