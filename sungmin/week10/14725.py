N = int(input())
info = list()
for _ in range(N):
    info.append(list(input().split())[1:])

cave = dict()
for i in info:
    d = cave
    for j in i:
        if j not in d.keys():
            d[j] = dict()
        d = d[j]

def print_dict(d:dict, rank):
    for key in sorted(d.keys()):
        print('--'*rank + key)
        print_dict(d[key], rank + 1)
print_dict(cave, 0)